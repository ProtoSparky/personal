import pandas as pd
import json

# Load JSON data
with open('output.json', 'r') as f:
    data = json.load(f)

# Transform JSON into a list of dictionaries
transformed_data = [{"Key": k, "Value": v} for d in data for k, v in d.items()]

# Convert the transformed data into a DataFrame
df = pd.DataFrame(transformed_data)

# Save the DataFrame as a CSV file
df.to_csv('output.csv', index=False)