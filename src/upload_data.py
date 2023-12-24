# %% Imports
import glob
import json
import os
import pprint
import redis
import xml.etree.ElementTree as ET
# %%
"""
Config Vars
"""
data_dir = '../example-data'
# %%
"""
Establish client
"""
# client = redis.Redis(host="localhost", port=6379, decode_responses=True)
# %%
def print_all_text(xml_file_path):
    fields = []

    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Iterate through all text elements in the XML
    for elem in root.iter():
        if elem.text and elem.text.strip():
            print(f"{elem.tag}: {elem.text.strip()}")
# %%
def parse_fields(xml_file_path):
    #FIXME: dummy field for some SPL's that do not label the document's initial title
    fields = [["dummy"]]

    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Iterate through all text elements in the XML
    for elem in root.iter():
        if elem.text and elem.text.strip():
            if "title" in elem.tag:
                fields.append([elem.text.strip()])
            elif "item" in elem.tag:
                fields[len(fields) - 1].append(elem.text)
            else:
                fields[len(fields) - 1].append(elem.text.strip())

    return fields
# %%
"""
Loop through each dir in the data dir folder.
Each drug entry dir is expected to follow the DailyMed structure
with one xml file per drug entry folder. This xml file holds the info
we will build our embedding based on.
"""

# Grab all files in the data source dir with an xml extension
xml_file_paths = glob.glob(f'{data_dir}/{"*"}/{"*.xml"}')

# parse all xml files to json
for i, xml_file_path in enumerate(xml_file_paths):
    fields = parse_fields(xml_file_path)
    for field in fields:
        if "USAGE" in field[0]:
            print(field)
# %%
    