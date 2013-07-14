import sys #imports sys module so file can be passed as arg from command line
import xml.etree.cElementTree as etree #imports etree to parse XML

# filename = sys.argv[1] #assigns second argument to filename - first is solution.py
tree = etree.parse('realRoutes.xml') #sets the passed xml file as the tree element
root = tree.getroot() #assigns the root of the xml file to root

routes = {}

for route in root.findall('table'):
  routes[route[4].text] = 0
print('cunt')

for route in root.findall('table'):
  routes[route[4].text] += 1

print(routes)
