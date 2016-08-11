import os
from lxml import etree

file_name = "2D.xml"
full_file = os.path.abspath(os.path.join('2D', file_name))
nodes = etree.parse(full_file)
NSMAP = {"mw": "urn:NEIDTRANS"}

hwd = nodes.findall(".//mw:HWD", namespaces=NSMAP)
for h in hwd:
    print(h.text)

meaning = nodes.findall(".//mw:MEANING", namespaces=NSMAP)
for m in meaning:
    print(m.text)

# etc...

print("========")
print("Bonanza!")
