import pandas as pd
import random
from faker import Faker

# Initialize
fake = Faker()
random.seed(42)

# Extended list of ICD-10 codes
icd10_codes = [
    ("E11.9", "Type 2 diabetes mellitus without complications"),
    ("I10", "Essential (primary) hypertension"),
    ("J45.909", "Unspecified asthma, uncomplicated"),
    ("E78.5", "Hyperlipidemia, unspecified"),
    ("F32.9", "Major depressive disorder, single episode, unspecified"),
    ("M54.5", "Low back pain"),
    ("R51", "Headache"),
    ("K21.9", "Gastro-esophageal reflux disease without esophagitis"),
    ("N39.0", "Urinary tract infection, site not specified"),
    ("G43.909", "Migraine, unspecified, not intractable, without status migrainosus"),
    ("Z00.00", "Encounter for general adult medical examination without abnormal findings"),
    ("J06.9", "Acute upper respiratory infection, unspecified"),
    ("B34.9", "Viral infection, unspecified"),
    ("R10.9", "Unspecified abdominal pain"),
    ("L03.90", "Cellulitis, unspecified"),
    ("H52.4", "Presbyopia"),
    ("E03.9", "Hypothyroidism, unspecified"),
    ("I25.10", "Atherosclerotic heart disease of native coronary artery without angina pectoris"),
    ("F41.1", "Generalized anxiety disorder"),
    ("Z79.899", "Other long term (current) drug therapy")
]

medications = [
    "Metformin", "Lisinopril", "Albuterol", "Atorvastatin", "Sertraline",
    "Levothyroxine", "Amlodipine", "Omeprazole", "Hydrochlorothiazide", "Gabapentin",
    "Losartan", "Fluticasone", "Ibuprofen", "Prednisone", "Simvastatin"
]

def generate_fhir_record(patient_id):
    gender = random.choice(["male", "female", "other"])
    birth_date = fake.date_of_birth(minimum_age=20, maximum_age=85).isoformat()
    condition_sample = random.sample(icd10_codes, k=random.randint(2, 5))
    condition_str = "; ".join([f"{code} ({desc})" for code, desc in condition_sample])
    med_sample = random.sample(medications, k=random.randint(1, 4))
    meds_str = "; ".join(med_sample)
    encounters = random.randint(1, 15)

    return {
        "patient_id": patient_id,
        "gender": gender,
        "birth_date": birth_date,
        "conditions": condition_str,
        "medications": meds_str,
        "encounters": encounters
    }

# Create dataset for 100 patients
data = [generate_fhir_record(f"PAT-{i+1:03d}") for i in range(1000)]
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("fhir_synthetic_records.csv", index=False)
print("FHIR records CSV generated: fhir_synthetic_records.csv")