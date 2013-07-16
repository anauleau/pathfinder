import sys #imports sys module so file can be passed as arg from command line
import xml.etree.cElementTree as etree #imports etree to parse XML
import json

# filename = sys.argv[1] #assigns second argument to filename - first is solution.py
# schema = etree.parse('schema.xml') #sets the passed xml file as the tree element
db = etree.parse('db.xml') #sets the passed xml file as the tree element
root = db.getroot() #assigns the root of the xml file to root

pathfinder = {
    "canoes": {},
    "codes": {},
    "paths": {},
    "people": {},
    "peopleRoles": {},
    "places": {},
    "tripCanoes": {},
    "tripPeople": {},
    "tripRoutes": {}
}


for table in root.findall('table'):
  if table.attrib['name'] == 'canoes':
    pathfinder['canoes'][table[1].text] = {}
    pathfinder['canoes'][table[1].text]['id'] = table[0].text
    pathfinder['canoes'][table[1].text]['name'] = table[1].text

  if table.attrib['name'] == 'codes':
    pathfinder['codes'][table[0].text] = {}
    pathfinder['codes'][table[0].text]['id'] = table[0].text
    pathfinder['codes'][table[0].text]['type'] = table[1].text
    pathfinder['codes'][table[0].text]['value'] = table[2].text

  if table.attrib['name'] == 'paths':
    pathfinder['paths'][table[0].text] = {}
    pathfinder['paths'][table[0].text]['id'] = table[0].text
    pathfinder['paths'][table[0].text]['fromTo'] = table[1].text
    pathfinder['paths'][table[0].text]['fromIdToId'] = table[2].text
    pathfinder['paths'][table[0].text]['frId'] = table[3].text
    pathfinder['paths'][table[0].text]['toId'] = table[4].text
    pathfinder['paths'][table[0].text]['type'] = table[5].text
    pathfinder['paths'][table[0].text]['color'] = table[6].text
    pathfinder['paths'][table[0].text]['portage'] = table[7].text
    pathfinder['paths'][table[0].text]['distance'] = table[8].text
    pathfinder['paths'][table[0].text]['time'] = table[9].text
    pathfinder['paths'][table[0].text]['track'] = table[10].text

  if table.attrib['name'] == 'people':
    pathfinder['people'][table[0].text] = {}
    pathfinder['people'][table[0].text]['id'] = table[0].text
    pathfinder['people'][table[0].text]['camperNum'] = table[1].text
    pathfinder['people'][table[0].text]['firstName'] = table[2].text
    pathfinder['people'][table[0].text]['lastName'] = table[3].text
    pathfinder['people'][table[0].text]['added'] = table[4].text

  if table.attrib['name'] == 'people_roles':
    pathfinder['peopleRoles'][table[0].text] = {}
    pathfinder['peopleRoles'][table[0].text]['id'] = table[0].text
    pathfinder['peopleRoles'][table[0].text]['personID'] = table[1].text
    pathfinder['peopleRoles'][table[0].text]['year'] = table[2].text
    pathfinder['peopleRoles'][table[0].text]['group'] = table[3].text

  if table.attrib['name'] == 'places':
    pathfinder['places'][table[1].text] = {}
    pathfinder['places'][table[1].text]['id'] = table[0].text
    pathfinder['places'][table[1].text]['name'] = table[1].text
    pathfinder['places'][table[1].text]['lat'] = table[2].text
    pathfinder['places'][table[1].text]['lon'] = table[3].text
    pathfinder['places'][table[1].text]['alt'] = table[4].text
    pathfinder['places'][table[1].text]['type'] = table[5].text
    pathfinder['places'][table[1].text]['jurisdiction'] = table[6].text

  if table.attrib['name'] == 'trip_canoes':
    pathfinder['tripCanoes'][table[0].text] = {}
    pathfinder['tripCanoes'][table[0].text]['id'] = table[0].text
    pathfinder['tripCanoes'][table[0].text]['canoeID'] = table[1].text
    pathfinder['tripCanoes'][table[0].text]['tripID'] = table[2].text
    pathfinder['tripCanoes'][table[0].text]['peID'] = table[3].text

  if table.attrib['name'] == 'trip_people':
    pathfinder['tripPeople'][table[0].text] = {}
    pathfinder['tripPeople'][table[0].text]['id'] = table[0].text
    pathfinder['tripPeople'][table[0].text]['tripID'] = table[1].text
    pathfinder['tripPeople'][table[0].text]['peID'] = table[2].text
    pathfinder['tripPeople'][table[0].text]['role'] = table[3].text

  if table.attrib['name'] == 'trip_routes':
    pathfinder['tripRoutes'][table[0].text] = {}
    pathfinder['tripRoutes'][table[0].text]['id'] = table[0].text
    pathfinder['tripRoutes'][table[0].text]['tripID'] = table[1].text
    pathfinder['tripRoutes'][table[0].text]['sequence'] = table[2].text
    pathfinder['tripRoutes'][table[0].text]['day'] = table[3].text
    pathfinder['tripRoutes'][table[0].text]['plId'] = table[4].text
    pathfinder['tripRoutes'][table[0].text]['truckTo'] = table[5].text
    pathfinder['tripRoutes'][table[0].text]['pickUp'] = table[6].text
    pathfinder['tripRoutes'][table[0].text]['camp'] = table[7].text

data = open('data.json', 'w')
pathfinder = json.dumps(pathfinder)
data.write(pathfinder)
print('done')
