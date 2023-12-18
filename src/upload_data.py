# %% Imports
import glob
import json
import os
import pprint
import redis
import xmltodict
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
client = redis.Redis(host="localhost", port=6379, decode_responses=True)
# %%
def extract_indications(spl_xml):
    # Parse the XML document
    tree = ET.fromstring(xml_string)

    # Find the title element
    title_element = tree.find('.//{urn:hl7-org:v3}title')  # Use the namespace in the XPath

    # Check if the title element exists
    if title_element is not None and title_element:
        # Accumulate text content from the title element's children
        title_text = ''.join(title_element.itertext()).strip()
        return title_text
    else:
        return "Title element not found."
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
    xml_file = open(xml_file_path)
    xml_string = xml_file.read()
    s = extract_indications(xml_string)
    print(s)
    break
# %%
