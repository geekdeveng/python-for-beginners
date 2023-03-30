"""
-author : geekdev
-desc : utils
"""

import (
    os, 
    json
)
from sys import platform
from typing import Any

def get_json_config() -> Any:
    """
    -desc   : This example assumes that info.json is being read.
    -param  : None
    -return : json object type.
    """
    
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        slash = "/"
    elif platform == "win32":
        slash = "\\"
        
    path = os.getcwd()        
    path += (slash + "info.json")
    
    with open(path) as f :
        config = json.load(f)
    
    return config