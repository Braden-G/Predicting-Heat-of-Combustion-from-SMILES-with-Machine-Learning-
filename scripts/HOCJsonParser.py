import csv
import json
import re


# Input JSON file path
json_file_path = "data/pubchemdata.json"
# Output CSV file path
output_csv = "data/pubchemFilteredDataNoKj.csv"
 
# Read JSON data from file
with open(json_file_path, "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)

# Function to extract relevant data
def extract_kj_mol_data(json_data):
    results = []
    annotations = json_data.get("Annotations", {}).get("Annotation", [])
    for annotation in annotations:
        source_id = annotation.get("SourceID")
        data_entries = annotation.get("Data", [])
        for data in data_entries:
            string_with_markup = data.get("Value", {}).get("StringWithMarkup", [])
            for entry in string_with_markup:
                value = entry.get("String", "")
                if re.search(r"kJ/mol", value, re.IGNORECASE):
                    match = re.search(r"(-?\d+(\.\d+)?)\s*kJ/mol", value, re.IGNORECASE)
                    if match:
                        value = match.group(1)
                    results.append({"SourceID": source_id, "Value": value})
    return results

# Extract the data
extracted_data = extract_kj_mol_data(json_data)

# Write the extracted data to a CSV
with open(output_csv, mode="w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write header
    csv_writer.writerow(["SourceID", "Value (kJ/mol)"])
    # Write rows
    for row in extracted_data:
        csv_writer.writerow([row["SourceID"], row["Value"]])

print(f"Data has been written to {output_csv}")