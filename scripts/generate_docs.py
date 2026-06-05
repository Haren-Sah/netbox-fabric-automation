import json
from pathlib import Path

with open("inventory/fabric.json") as f:
    fabric = json.load(f)

with open("inventory/topology.json") as f:
    topology = json.load(f)

Path("docs").mkdir(
    exist_ok=True
)

report = []

report.append("# NetBox Fabric Automation Report\n")

report.append("## Device Inventory\n")

report.append(
    "| Device | Role | Vendor | ASN | Loopback |"
)

report.append(
    "|----------|----------|----------|----------|----------|"
)

for hostname, device in sorted(fabric.items()):

    report.append(
        f"| {hostname} "
        f"| {device['role']} "
        f"| {device['vendor']} "
        f"| {device['asn']} "
        f"| {device['loopback']} |"
    )

report.append("\n")

report.append("## Physical Topology\n")

for hostname, data in sorted(topology.items()):

    report.append(
        f"### {hostname}\n"
    )

    report.append(
        "| Local Interface | Remote Device | Remote Interface |"
    )

    report.append(
        "|----------------|---------------|------------------|"
    )

    for neighbor in data["neighbors"]:

        report.append(
            f"| {neighbor['local_interface']} "
            f"| {neighbor['remote_device']} "
            f"| {neighbor['remote_interface']} |"
        )

    report.append("\n")

with open(
    "docs/fabric_report.md",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "\n".join(report)
    )

print(
    "Fabric report generated."
)