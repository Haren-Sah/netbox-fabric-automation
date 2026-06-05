import json
import pynetbox

from inventory.config import (
    NETBOX_URL,
    NETBOX_TOKEN
)

nb = pynetbox.api(
    NETBOX_URL,
    token=NETBOX_TOKEN
)

topology = {}

devices = nb.dcim.devices.all()

for device in devices:

    topology[device.name] = {
        "neighbors": []
    }

    interfaces = nb.dcim.interfaces.filter(
        device_id=device.id
    )

    for interface in interfaces:

        try:

            if not interface.connected_endpoints:
                continue

            remote = interface.connected_endpoints[0]

            topology[device.name]["neighbors"].append({
                "local_interface": interface.name,
                "remote_device": remote.device.name,
                "remote_interface": remote.name,
                "remote_asn": None 
            })

        except Exception:
            pass

with open(
    "inventory/topology.json",
    "w"
) as f:

    json.dump(
        topology,
        f,
        indent=4
    )

print("Topology exported.")