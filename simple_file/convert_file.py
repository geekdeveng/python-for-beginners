"""
-author : geekdev
-desc : file libarary
"""

import json
import yaml
from typing import Any


class ConvertFile:
    """
    yaml to json , json to yaml Library classes related to conversion.
    """
    
    def __init__(self) -> None:
        pass
    
    def read_yaml_file(self, file_name: str) -> Any:
        """
        -desc               : read from yaml file
        -param file_name    : yaml file path
        -return             : yaml object
        """
        
        with open(file_name, "r") as file:
            return yaml.safe_load(file)

    def convert_yaml_obj_to_json_str(self, yaml_obj: Any) -> str:
        """
        -desc           : yaml object to json str.
        -param yaml_obj : yaml object
        -return         : json str
        """
        
        return json.dumps(yaml_obj)
        
    def convert_json_str_to_json_obj(self, json_str: str) -> Any:
        """
        -desc           : json string to json object.
        -param json_str : json string
        -return         : json object
        """
        
        return json.loads(json_str)
            
    def write_json_to_yaml_file(self, file_name: str, json_obj: Any) -> None:
        """
        -desc               : Write json object to yaml file
        -param file_name    : json file path
        -param yaml_obj     : yaml object
        -return             : None
        """
        
        with open(file_name, "w") as file :
            yaml.dump(json_obj, file)
