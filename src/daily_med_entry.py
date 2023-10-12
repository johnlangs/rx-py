from collections import OrderedDict
from dataclasses import dataclass
from typing import Any

@dataclass
class dailyMedEntry:
    """
    Used to store information about one Daily Med Entry.
    Created after parsing an entry.
    """

    entry_total_size: bytes # Total size of an entry's data, in bytes. Includes both xml entry and images
    path: str # path to entry's original folder

    xml_file_path: str
    parsed_xml_file: OrderedDict[str, Any] # dictonary representation of xml data
    images: list[str] # list of paths to all images for an ind

    def __init__(self, path: str):
        self.path = path
