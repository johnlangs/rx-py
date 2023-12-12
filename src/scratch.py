import xmltodict
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

file = open("example-data/20230801_0d40e68d-feb5-4061-8b43-515b2f553371/a6e02619-a4ee-4603-ad7a-c60187412f1a.xml")
file_string = file.read()
xml = xmltodict.parse(file_string)
print(json.dumps(xml))