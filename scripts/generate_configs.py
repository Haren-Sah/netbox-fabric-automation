import json
from pathlib import Path

from jinja2 import (
    Environment,
    FileSystemLoader
)

env = Environment(
    loader=FileSystemLoader("templates")
)

with open("inventory/fabric.json") as f:
    fabric = json.load(f)

with open("inventory/topology.json") as f:
    topology = json.load(f)

Path("generated_configs").mkdir(
    exist_ok=True
)

for hostname, device in fabric.items():

    vendor = device["vendor"].lower()
    role = device["role"].lower()

    template_name = (
        f"{vendor}_{role}.j2"
    )

    template = env.get_template(
        template_name
    )

    neighbors = []

    for neighbor in topology[hostname]["neighbors"]:

        remote_device = neighbor["remote_device"]

        neighbors.append(
            {
                "remote_device": remote_device,
                "remote_asn": fabric[
                    remote_device
                ]["asn"]
            }
        )

    config = template.render(
        hostname=hostname,
        asn=device["asn"],
        loopback=device["loopback"],
        neighbors=neighbors
    )

    with open(
        f"generated_configs/{hostname}.cfg",
        "w"
    ) as f:

        f.write(config)

print("Configs generated.")