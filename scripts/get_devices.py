import pynetbox

from inventory.config import (
    NETBOX_URL,
    NETBOX_TOKEN
)

nb = pynetbox.api(
    NETBOX_URL,
    token=NETBOX_TOKEN
)

devices = nb.dcim.devices.all()

for device in devices:
    print(
        f"Name: {device.name}"
    )