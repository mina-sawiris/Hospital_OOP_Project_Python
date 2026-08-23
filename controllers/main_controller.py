import os

from controllers.hospital_controller import HospitalController
from controllers.data_handler import Save_data, Load_data
from views.main_window import MainWindow
from views.add_patient_dialog import AddPatientDialog
from views.add_staff_dialog import AddStaffDialog
from views.add_department_dialog import AddDepartmentDialog


# data/hospital_data.json, resolved relative to this file so it works no
# matter what directory the app is launched from.
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(_PROJECT_ROOT, "data", "hospital_data.json")

VALID_STATUSES = ("Stable", "Observation", "Critical")


class MainController:
    """
    The 'glue' of the app.

    It owns the HospitalController (models) and the MainWindow (view), and
    is the only place that talks to both. Whenever something happens in the
    GUI, a method here updates the model and then refreshes the view, so the
    two never drift out of sync.
    """

    def __init__(self):
        # ---- 1. Load saved state, or start fresh ----
        loaded_hospital = Load_data(DATA_FILE)

        if loaded_hospital is not None:
            self.hospital_controller = HospitalController(hospital=loaded_hospital)
        else:
            self.hospital_controller = HospitalController("MediCare Hospital", "Unknown")
            # Seed a couple of default departments so the app isn't empty
            # the very first time someone runs it.
            self.hospital_controller.add_department("Cardiology")
            self.hospital_controller.add_department("Pediatrics")

        # ---- 2. Build the view ----
        self.window = MainWindow()
        self.current_view = "patients"  # "patients" or "staff"

        # ---- 3. Wire GUI events to controller actions ----
        self._connect_events()

        # ---- 4. Paint real data over the view's placeholder content ----
        self._refresh_departments()
        self._refresh_table()

        # ---- 5. Persist state when the window is closed ----
        self.window.protocol("WM_DELETE_WINDOW", self._on_close)

    def run(self):
        self.window.mainloop()

    # ------------------------------------------------------------------
    # Wiring
    # ------------------------------------------------------------------
    def _connect_events(self):
        # The sidebar's Patients/Staff buttons already switch the table's
        # columns via show_patients_view/show_staff_view. We wrap those
        # methods so that, right after the view rebuilds its (placeholder)
        # rows, the controller immediately overwrites them with real data.
        self._wrap_view_method("show_patients_view", self._on_show_patients)
        self._wrap_view_method("show_staff_view", self._on_show_staff)
        
        self.window.btn_patients.configure(command=self.window.show_patients_view)
        self.window.btn_staff.configure(command=self.window.show_staff_view)

        self.window.add_dept_btn.configure(command=self._open_add_department_dialog)
        self.window.add_record_btn.configure(command=self._open_add_record_dialog)
        self.window.dept_dropdown.configure(command=self._on_department_selected)

    def _wrap_view_method(self, method_name, after_callback):
        """Call the view's existing method, then run our own refresh logic
        right after it, without needing to edit views/main_window.py."""
        original_method = getattr(self.window, method_name)

        def wrapped(*args, **kwargs):
            original_method(*args, **kwargs)
            after_callback()

        setattr(self.window, method_name, wrapped)

    # ------------------------------------------------------------------
    # Navigation (Patients / Staff tabs)
    # ------------------------------------------------------------------
    def _on_show_patients(self):
        self.current_view = "patients"
        self._refresh_table()

    def _on_show_staff(self):
        self.current_view = "staff"
        self._refresh_table()

    def _on_department_selected(self, _choice):
        self._refresh_table()

    # ------------------------------------------------------------------
    # Departments
    # ------------------------------------------------------------------
    def _refresh_departments(self):
        departments = self.hospital_controller.get_departments()
        names = [department.name for department in departments]

        if not names:
            names = ["No Departments"]

        current_selection = self.window.dept_dropdown.get()
        self.window.dept_dropdown.configure(values=names)

        if current_selection not in names:
            self.window.dept_dropdown.set(names[0])

    def _open_add_department_dialog(self):
        AddDepartmentDialog(
            self.window,
            on_department_added=self._handle_department_added,
            dark_mode=self.window.theme_switch.get() == 1,
        )

    def _handle_department_added(self, department):
        added = self.hospital_controller.add_existing_department(department)

        if not added:
            return

        self._refresh_departments()
        self.window.dept_dropdown.set(department.name)
        self._refresh_table()

    # ------------------------------------------------------------------
    # Patients / Staff records
    # ------------------------------------------------------------------
    def _open_add_record_dialog(self):
        department_name = self.window.dept_dropdown.get()
        dark_mode = self.window.theme_switch.get() == 1

        if self.hospital_controller.find_department(department_name) is None:
            self._show_no_department_warning()
            return

        if self.current_view == "patients":
            AddPatientDialog(
                self.window,
                on_patient_added=lambda patient: self._handle_patient_added(department_name, patient),
                dark_mode=dark_mode,
            )
        else:
            AddStaffDialog(
                self.window,
                on_staff_added=lambda staff: self._handle_staff_added(department_name, staff),
                dark_mode=dark_mode,
            )

    def _show_no_department_warning(self):
        from tkinter import messagebox
        messagebox.showwarning(
            "No Department Selected",
            "Please add or select a department before adding records.",
            parent=self.window,
        )

    def _handle_patient_added(self, department_name, patient):
        if self.hospital_controller.add_existing_patient(department_name, patient):
            self._refresh_table()

    def _handle_staff_added(self, department_name, staff_member):
        if self.hospital_controller.add_existing_staff(department_name, staff_member):
            self._refresh_table()

    # ------------------------------------------------------------------
    # Table rendering
    # ------------------------------------------------------------------
    def _refresh_table(self):
        department_name = self.window.dept_dropdown.get()
        table = self.window.table

        for row in table.get_children():
            table.delete(row)

        if self.current_view == "patients":
            for patient in self.hospital_controller.get_patients(department_name):
                status = patient.status if patient.status in VALID_STATUSES else "Stable"
                table.insert(
                    "", "end",
                    values=(patient.name, patient.patient_id, patient.age,
                            patient.medical_record, patient.room, f"\u25CF {patient.status}"),
                    tags=(status,),
                )
        else:
            for staff_member in self.hospital_controller.get_staff(department_name):
                table.insert(
                    "", "end",
                    values=(staff_member.name, staff_member.age, staff_member.position),
                )

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    def _on_close(self):
        Save_data(self.hospital_controller.hospital, DATA_FILE)
        self.window.destroy()
