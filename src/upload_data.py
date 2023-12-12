# %% Imports
import glob
import json
import os
import pprint
import redis
import xmltodict
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
def store_nested_data(redis_client, redis_key, data):
    """
    Recursively stores nested data in Redis.
    """
    if isinstance(data, dict):
        # If it's a dictionary, iterate through key-value pairs
        for key, value in data.items():
            # Recursively store nested data
            store_nested_data(redis_client, f"{redis_key}:{key}", value)
    elif isinstance(data, list):
        # If it's a list, iterate through the elements
        for index, element in enumerate(data):
            # Recursively store nested data
            store_nested_data(redis_client, f"{redis_key}[{index}]", element)
    else:
        # If it's a leaf node, store the value
        redis_client.hset(redis_key, "value", json.dumps(data))
# %%
"""
Loop through each dir in the data dir folder.
Each drug entry dir is expected to follow the DailyMed structure
with one xml file per drug entry folder. This xml file holds the info
we will build our embedding based on.
"""

# Grab all files in the data source dir with an xml extension
xml_file_paths = glob.glob(f'{data_dir}/{"*"}/{"*.xml"}')
pp = pprint.PrettyPrinter(indent=4)
# parse all xml files to json
for i, xml_file_path in enumerate(xml_file_paths):
    xml_file = open(xml_file_path)
    dict_file = xmltodict.parse(xml_file.read())
    print(dict_file)
    with open('./out.txt', 'w') as file:
        file.write(pp.pformat(dict_file))

    break

    redis_key = f"test_2:{i:03}"
    store_nested_data(client, redis_key, dict_file)




# %%
