import sys #imports sys module so file can be passed as arg from command line
import xml.etree.cElementTree as etree #imports etree to parse XML

# filename = sys.argv[1] #assigns second argument to filename - first is solution.py
# schema = etree.parse('schema.xml') #sets the passed xml file as the tree element
db = etree.parse('db.xml') #sets the passed xml file as the tree element
root = tree.getroot() #assigns the root of the xml file to root

pathfinder = {
    "admin": {},
    "canoes": {},
    "codes": {},
    "paths": {},
    "peopleRoles": {},
    "places": {},
    "trips": {},
    "tripCanoes": {},
    "tripPeople": {},
    "tripRoutes": {},
    "xLog": {},
    "xVLog": {}
}

# new obj for each table
# for each column in row insert in to obj


# for table in schema.findall('table'):
#     pathfincer[table.name] = {}
print(pathfinder)

