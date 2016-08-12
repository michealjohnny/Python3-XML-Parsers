import os
from lxml import etree

file_name = "2D.xml"
full_file = os.path.abspath(os.path.join('2D', file_name))
nodes = etree.parse(full_file)
NSMAP = {"mw": "urn:NEIDTRANS"}

#==========================================================
#comment out unwanted blocks

hwd = nodes.findall(".//mw:HWD", namespaces=NSMAP)
for h in hwd:
    print(h.text)

release = nodes.findall(".//mw:RELEASE", namespaces=NSMAP)
for r in release:
        if r.text == "G":
            print(r.text)

meaning = nodes.findall(".//mw:MEANING", namespaces=NSMAP)
for m in meaning:
    print(m.text)

#==========================================================
#comment out unwanted blocks

release = nodes.findall(".//mw:RELEASE", namespaces=NSMAP)
hwd = nodes.findall(".//mw:HWD", namespaces=NSMAP)
for h in hwd:
    for r in release:
        if r.text == "G":
            print("* {} [{}] ".format(h.text, r.text))
        else:
            break

# etc...

print("========")
print("Bonanza!")
