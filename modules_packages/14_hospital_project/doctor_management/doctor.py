def register_doctor(doctors, doctor_id, name, specialization):
    doctors.append({"id": doctor_id, "name": name, "specialization": specialization})

def find_doctor(doctors, doctor_id):
    for d in doctors:
        if d["id"] == doctor_id:
            return d
    return None
