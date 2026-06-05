# NetBox Fabric Automation Report

## Device Inventory

| Device | Role | Vendor | ASN | Loopback |
|----------|----------|----------|----------|----------|
| LEAF1 | Leaf | Cisco | 65101 | 10.255.1.1 |
| LEAF2 | Leaf | Arista | 65102 | 10.255.1.2 |
| SPINE1 | Spine | Cisco | 65001 | 10.255.0.1 |
| SPINE2 | Spine | Arista | 65002 | 10.255.0.2 |


## Physical Topology

### LEAF1

| Local Interface | Remote Device | Remote Interface |
|----------------|---------------|------------------|
| Ethernet1 | SPINE1 | Ethernet1 |
| Ethernet2 | SPINE2 | Ethernet1 |


### LEAF2

| Local Interface | Remote Device | Remote Interface |
|----------------|---------------|------------------|
| Ethernet1 | SPINE1 | Ethernet2 |
| Ethernet2 | SPINE2 | Ethernet2 |


### SPINE1

| Local Interface | Remote Device | Remote Interface |
|----------------|---------------|------------------|
| Ethernet1 | LEAF1 | Ethernet1 |
| Ethernet2 | LEAF2 | Ethernet1 |


### SPINE2

| Local Interface | Remote Device | Remote Interface |
|----------------|---------------|------------------|
| Ethernet1 | LEAF1 | Ethernet2 |
| Ethernet2 | LEAF2 | Ethernet2 |

