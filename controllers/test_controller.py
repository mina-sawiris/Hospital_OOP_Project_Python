from controllers.hospital_controller import HospitalController


controller = HospitalController(
    name="CHC Hospital",
    location="Cairo"
)

controller.add_department("Cardiology")

department = controller.find_department("Cardiology")

print("Department:", department.name)

result = controller.add_patient(
    department_name="Cardiology",
    name="Ahmed Ali",
    age=30,
    medical_record="Diabetes",
    room="3A-12",
    status="Stable"
)

print("Patient added:", result)

print("Patients:")

for patient in department.patients:
    print(patient.view_info())