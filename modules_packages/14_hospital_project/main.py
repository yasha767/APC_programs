from patient_management import patient
from doctor_management import doctor
from billing import bill
from medical_records import records

patients = []
doctors = []
medical_records_list = []

patient.register_patient(patients, 1, "Ravi", 30)
doctor.register_doctor(doctors, 1, "Dr. Sharma", "Cardiology")

p = patient.find_patient(patients, 1)
d = doctor.find_doctor(doctors, 1)

records.add_record(medical_records_list, 1, "Fever", "Paracetamol")

print("Patient:", p)
print("Doctor:", d)
print("Records:", records.get_records(medical_records_list, 1))

bill.generate_bill(p, 500, 200)
