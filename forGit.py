import os
from lxml import etree
from bs4 import BeautifulSoup

output = open("C:/Users/UserName/Desktop/Folder/output.txt", "w", encoding="utf-8")

soup_xml = BeautifulSoup(open("MyXml.xml", encoding="utf-8"), features="xml")
# beautifulSoup4 works best when your feature tells it if you're parsing
# xml or html to it

counter = 0
MyTag = soup_xml.find_all("MyTag")
for h in MyTag:
    counter += 1
    h = str(h.encode("utf-8"))
    output.write(h + "\n")
    #print(counter, h)

# I find beautiful soup to be a bit more lenient when searching children
# and dealing with namespaces than using lxml directly
# (because Beautiful Soup uses lxml in the background!)
