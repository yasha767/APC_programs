def add_record(records, patient_id, diagnosis, treatment):
    records.append({"patient_id": patient_id, "diagnosis": diagnosis, "treatment": treatment})

def get_records(records, patient_id):
    return [r for r in records if r["patient_id"] == patient_id]
