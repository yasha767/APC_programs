def register_patient(patients, patient_id, name, age):
    patients.append({"id": patient_id, "name": name, "age": age})

def find_patient(patients, patient_id):
    for p in patients:
        if p["id"] == patient_id:
            return p
    return None
