import json

with open("inventory/topology.json") as f:
    topology = json.load(f)

lines = []

lines.append("graph TD")
lines.append("")

added_links = set()

for device, data in topology.items():

    for neighbor in data["neighbors"]:

        local = device
        remote = neighbor["remote_device"]

        key = tuple(
            sorted(
                [local, remote]
            )
        )

        if key in added_links:
            continue

        added_links.add(key)

        lines.append(
            f"{local} --- {remote}"
        )

with open(
    "docs/topology.mmd",
    "w"
) as f:

    f.write(
        "\n".join(lines)
    )

print(
    "Topology diagram generated."
)