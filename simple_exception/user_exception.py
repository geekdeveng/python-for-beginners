"""
-author : geekdev
-desc : utils
"""

class UserException(Exception):
    """
    User Exception
    """
    
    def __init__(self, msg: str) -> None:
        """
        -desc   : init function
        -param  : User Exception MSG
        -return : None
        """
        
        super().__init__(msg)
