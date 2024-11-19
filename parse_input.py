import csv
import yaml

def parse_input(input_file, output_file):
    inventory = {"inventory_hosts": []}
    with open(input_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            # Skip invalid rows
            if len(row) < 2:
                print(f"Skipping invalid row: {row}")
                continue

            # Strip whitespace and construct inventory entry
            entry = {
                "ip": row[0].strip(),
                "hostname": row[1].strip()
            }
            if len(row) > 2:  # Optional location
                entry["location"] = row[2].strip()
            inventory["inventory_hosts"].append(entry)

    # Save inventory as YAML
    with open(output_file, "w") as f:
        yaml.dump(inventory, f)

# Example usage
parse_input("input.csv", "inventory.yaml")
