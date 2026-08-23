from models.hospital import Hospital
from models.patient import Patient
from models.staff import Staff
from models.department import Department

class HospitalController:

    def __init__(self, name: str = "New Hospital", location: str = "Unknown", hospital: Hospital = None):
        # If a Hospital object was already built (e.g. loaded from the JSON
        # file by data_handler.Load_data), reuse it instead of creating a
        # brand-new empty one. This is what lets MainController hand the
        # loaded state straight to the controller on startup.
        self.hospital = hospital if hospital is not None else Hospital(name, location)


    def add_department(self, name: str):
        department = Department(name)
        self.hospital.add_department(department)
        return department


    def add_existing_department(self, department: Department) -> bool:
        """Register a Department object that was already built elsewhere
        (e.g. by AddDepartmentDialog in the views layer)."""
        if self.find_department(department.name) is not None:
            return False

        self.hospital.add_department(department)
        return True


    def add_existing_patient(self, department_name: str, patient: Patient) -> bool:
        """Attach an already-built Patient object (e.g. from AddPatientDialog)
        to the given department."""
        department = self.find_department(department_name)

        if department is None:
            return False

        department.add_patient(patient)
        return True


    def add_existing_staff(self, department_name: str, staff_member: Staff) -> bool:
        """Attach an already-built Staff object (e.g. from AddStaffDialog)
        to the given department."""
        department = self.find_department(department_name)

        if department is None:
            return False

        department.add_staff(staff_member)
        return True

        
    def find_department(self, name: str):
        for department in self.hospital.departments:
            if department.name == name:
                return department

        return None
    
    
    def add_patient(self,department_name: str,name: str,age: int,medical_record: str,room: str = "N/A",status: str = "Stable"):
        department = self.find_department(department_name)

        if department is None:
            return False

        patient = Patient(name=name,age=age,medical_record=medical_record,room=room,status=status)

        department.add_patient(patient)

        return True
    
    def add_staff(self,department_name: str,name: str,age: int,position: str):
        department = self.find_department(department_name)

        if department is None:
            return False

        staff = Staff(name=name, age=age,position=position)

        department.add_staff(staff)

        return True
    
    def get_departments(self):
        return self.hospital.departments

    def get_patients(self, department_name: str):
        department = self.find_department(department_name)

        if department is None:
            return []

        return department.patients

    def get_staff(self, department_name: str):
        department = self.find_department(department_name)

        if department is None:
            return []

        return department.staff
    
    