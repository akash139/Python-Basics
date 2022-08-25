import re
desc = "Node Name: mu-bam-r3\nNode IP Address: 10.11.12.13\nStacked Switch Number: 1\nData Ring Status Description: Warning\nMember Count : 2\nSwitch Status Description: Switch Stack status is Warning, Data Ring status is Warning, Power Rings overall status is Unknown.\nMachine Type(Device Model) : Catalyst 37xx Stack'"
nodeName = re.findall("Node Name.*", desc)
nodeIP = re.findall("Node IP Address.*", desc)
stackedSwitch= re.findall("Stacked Switch Number.*", desc)
print(nodeName[0].split(':')[1].strip())
print(nodeIP[0].split(':')[1].strip())
print(stackedSwitch[0].split(':')[1].strip())
