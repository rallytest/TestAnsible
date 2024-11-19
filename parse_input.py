import csv
import yaml

def parse_input(input_file, output_file):
    inventory = {"hosts": []}
    with open(input_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            entry = {
                "ip": row[0],
                "hostname": row[1]
            }
            if len(row) > 2:  # Optional location
                entry["location"] = row[2]
            inventory["hosts"].append(entry)
    
    with open(output_file, "w") as f:
        yaml.dump(inventory, f)

# Example usage
parse_input("input.csv", "inventory.yaml")

