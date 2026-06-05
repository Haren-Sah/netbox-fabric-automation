import json
import re

with open("inventory/topology.json") as f:
    topology = json.load(f)

results = []

for device, data in topology.items():

    config_file = (
        f"generated_configs/{device}.cfg"
    )

    with open(config_file) as cfg:
        config = cfg.read()

    discovered_neighbors = []

    for match in re.findall(
        r"neighbor (\S+) remote-as",
        config
    ):
        discovered_neighbors.append(match)

    intended_neighbors = []

    for neighbor in data["neighbors"]:
        intended_neighbors.append(
            neighbor["remote_device"]
        )

    intended_neighbors.sort()
    discovered_neighbors.sort()

    if intended_neighbors == discovered_neighbors:

        results.append(
    {
        "device": device,
        "status": "PASS",
        "expected": intended_neighbors,
        "actual": discovered_neighbors
    }
)

    else:

        results.append(
            (
                device,
                "FAIL"
            )
        )

print("\nValidation Results\n")

for result in results:

    print(
        f"\nDevice: {result['device']}"
    )

    print(
        f"Status: {result['status']}"
    )

    print(
        f"Expected: {result['expected']}"
    )

    print(
        f"Actual: {result['actual']}"
    )