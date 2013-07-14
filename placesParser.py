import sys #imports sys module so file can be passed as arg from command line
import xml.etree.cElementTree as etree #imports etree to parse XML

# filename = sys.argv[1] #assigns second argument to filename - first is solution.py
tree = etree.parse('routes.xml') #sets the passed xml file as the tree element
root = tree.getroot() #assigns the root of the xml file to root

places = {}
lat = 'lat'
lon = 'lon'

for place in root.findall('table'):
  places[place[0].text] = {}
  places[place[0].text]['name'] = place[1].text
  places[place[0].text]['lat']  = place[2].text
  places[place[0].text]['lon']  = place[3].text

print(places)

