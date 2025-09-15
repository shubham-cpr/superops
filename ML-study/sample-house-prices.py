import pandas as pd
import random

# Sample data to generate
locations = ["Seattle", "San Francisco", "Austin", "Chicago", "Miami", "Denver", "New York", "Boston"]
conditions = ["Excellent", "Good", "Fair", "Poor"]

def generate_house_record(id):
    location = random.choice(locations)
    size = random.randint(800, 4000)  # in sqft
    bedrooms = random.randint(1, 5)
    bathrooms = random.randint(1, 4)
    year_built = random.randint(1970, 2022)
    garage = random.choice(["Yes", "No"])
    condition = random.choices(conditions, weights=[0.3, 0.4, 0.2, 0.1])[0]

    # Simple pricing model (randomized)
    base_price = size * random.randint(150, 300)
    condition_factor = {"Excellent": 1.2, "Good": 1.0, "Fair": 0.85, "Poor": 0.7}[condition]
    garage_bonus = 10000 if garage == "Yes" else 0
    price = int(base_price * condition_factor + garage_bonus)

    return {
        "ID": id,
        "Location": location,
        "Size (sqft)": size,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Year Built": year_built,
        "Garage": garage,
        "Condition": condition,
        "Price (USD)": price
    }

# Generate records for 100 houses
data = [generate_house_record(i + 1) for i in range(1000)]
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("sample_house_prices.csv", index=False)
print("House price dataset generated: sample_house_prices.csv")