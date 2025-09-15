import pandas as pd
import random
from faker import Faker
import datetime

# Initialize
fake = Faker()
random.seed(42)

# Sample list of vital signs and lab results for LHR (Longitudinal Health Record)
vitals = ["blood_pressure", "heart_rate", "respiratory_rate", "temperature", "oxygen_saturation"]
labs = ["glucose", "hemoglobin", "creatinine", "cholesterol", "WBC"]

# Function to generate a single patient's time-series LHR data
def generate_lhr_timeseries(patient_id, start_date, num_days):
    records = []
    base_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    for i in range(num_days):
        current_date = base_date + datetime.timedelta(days=i)
        record = {
            "patient_id": patient_id,
            "date": current_date.date().isoformat(),
            "blood_pressure": f"{random.randint(100, 140)}/{random.randint(60, 90)}",
            "heart_rate": random.randint(60, 100),
            "respiratory_rate": random.randint(12, 20),
            "temperature": round(random.uniform(36.5, 38.5), 1),
            "oxygen_saturation": random.randint(95, 100),
            "glucose": random.randint(70, 150),
            "hemoglobin": round(random.uniform(12, 17), 1),
            "creatinine": round(random.uniform(0.6, 1.5), 2),
            "cholesterol": random.randint(150, 250),
            "WBC": round(random.uniform(4.0, 11.0), 1)
        }
        records.append(record)
    return records

# Generate time-series LHR data for 10 patients over 30 days
all_data = []
for i in range(1000):
    patient_id = f"PAT-{i+1:03d}"
    lhr_records = generate_lhr_timeseries(patient_id, start_date="2024-01-01", num_days=30)
    all_data.extend(lhr_records)

# Create DataFrame and export
lhr_df = pd.DataFrame(all_data)
lhr_df.to_csv("lhr_timeseries_data.csv", index=False)
print("LHR time-series CSV generated: lhr_timeseries_data.csv")