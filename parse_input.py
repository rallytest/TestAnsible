import yaml
import csv

def parse_input(input_file, output_file):
    inventory_hosts = []
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            inventory_hosts.append({
                "ip": row.get("ip", "").strip(),
                "hostname": row.get("hostname", "").strip(),
                "location": row.get("location", "").strip()
            })

    with open(output_file, 'w') as yamlfile:
        yaml.dump({"inventory_hosts": inventory_hosts}, yamlfile, default_flow_style=False)

parse_input("input.csv", "inventory.yaml")

