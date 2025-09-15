import pandas as pd
import random
from faker import Faker

# Initialize
fake = Faker()
random.seed(42)

# Sample data
icd10_conditions = [
    ("E11.9", "Type 2 diabetes mellitus without complications"),
    ("I10", "Essential (primary) hypertension"),
    ("J45.909", "Unspecified asthma, uncomplicated"),
    ("E78.5", "Hyperlipidemia, unspecified"),
    ("M54.5", "Low back pain")
]

lab_tests = ["Hemoglobin", "Cholesterol", "Blood Glucose", "Creatinine", "WBC Count"]

# Generator function
def generate_lhr_record(patient_id):
    gender = random.choice(["Male", "Female", "Other"])
    birth_date = fake.date_of_birth(minimum_age=20, maximum_age=90).isoformat()

    num_visits = random.randint(3, 10)
    visits = sorted([fake.date_between(start_date='-5y', end_date='today') for _ in range(num_visits)])
    visits_str = "; ".join(date.isoformat() for date in visits)

    lab_results = []
    for visit_date in visits:
        test = random.choice(lab_tests)
        value = round(random.uniform(3.0, 200.0), 2)
        lab_results.append(f"{visit_date.isoformat()} - {test}: {value}")
    lab_results_str = "; ".join(lab_results)

    diagnosis_history = random.sample(icd10_conditions, k=random.randint(1, 3))
    diagnoses_str = "; ".join([f"{code} ({desc})" for code, desc in diagnosis_history])

    return {
        "patient_id": patient_id,
        "gender": gender,
        "birth_date": birth_date,
        "visits": visits_str,
        "lab_results": lab_results_str,
        "diagnoses": diagnoses_str
    }

# Generate dataset
records = [generate_lhr_record(f"PAT-{i+1:03d}") for i in range(1000)]
df = pd.DataFrame(records)

# Save as CSV
df.to_csv("lhr_only_dataset_1000_patients.csv", index=False)
print("CSV file generated: lhr_only_dataset_1000_patients.csv")
