from models.hospital import Hospital
from models.patient import Patient
from models.staff import Staff
from models.department import Department

class HospitalController:

    def __init__(self, name: str, location: str):
        self.hospital = Hospital(name, location)
        
        
    def add_department(self, name: str):
        department = Department(name)
        self.hospital.add_department(department)
        
        
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
    
    