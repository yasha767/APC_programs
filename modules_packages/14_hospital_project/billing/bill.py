def generate_bill(patient, consultation_fee, medicine_cost):
    total = consultation_fee + medicine_cost
    print(f"Bill for {patient['name']}: Consultation {consultation_fee} + Medicine {medicine_cost} = {total}")
    return total
