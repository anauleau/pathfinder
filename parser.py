import sys #imports sys module so file can be passed as arg from command line
import xml.etree.cElementTree as etree #imports etree to parse XML

# filename = sys.argv[1] #assigns second argument to filename - first is solution.py
# schema = etree.parse('schema.xml') #sets the passed xml file as the tree element
db = etree.parse('db.xml') #sets the passed xml file as the tree element
root = db.getroot() #assigns the root of the xml file to root

pathfinder = {
    "canoes": {},
    "codes": {},
    "paths": {},
    "peopleRoles": {},
    "places": {},
    "tripCanoes": {},
    "tripPeople": {},
    "tripRoutes": {},
    "xLog": {},
    "xVLog": {}
}


for table in root.findall('table'):
  if table.attrib['name'] == 'Admin':
    print table[1].text

