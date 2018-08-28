import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
xmlp = ET.XMLParser(encoding="utf-8")
f = ET.parse('./xml/00000004.xml',parser=xmlp)
root = f.getroot()
for parent in root.getiterator():
    for child in parent:
        
        if child.tag == 'generic.name':
            print(child.text)
        if child.tag == 'piid':
            print(child.get('id'))
            print(child.get('branch'))

#childs = root[0].getiterator()
#print()
#print(child.find('detail_unit'))