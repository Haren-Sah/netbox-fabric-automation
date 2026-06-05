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

LOOPBACKS = {
    "SPINE1": "10.255.0.1",
    "SPINE2": "10.255.0.2",
    "LEAF1": "10.255.1.1",
    "LEAF2": "10.255.1.2"
}

fabric = {}

devices = nb.dcim.devices.all()

for device in devices:

    fabric[device.name] = {
        "role": device.role.name,
        "vendor": device.device_type.manufacturer.name,
        "model": device.device_type.model,
        "asn": device.custom_fields.get("bgp_asn"),
        "loopback": LOOPBACKS.get(device.name)
    }

with open(
    "inventory/fabric.json",
    "w"
) as f:

    json.dump(
        fabric,
        f,
        indent=4
    )

print("Fabric inventory exported.")