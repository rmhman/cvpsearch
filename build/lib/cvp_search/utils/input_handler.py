from typing import Optional

def get_search_string(cmd_arg: Optional[str] = None) -> str:
    """
    Get the search string from either command line argument or user input
    
    Args:
        cmd_arg: Optional command line argument
        
    Returns:
        str: The search string to use
        
    Raises:
        ValueError: If the provided string is empty or only whitespace
    """
    search_string = cmd_arg if cmd_arg else input("Enter search string: ").strip()
    
    if not search_string:
        raise ValueError("Search string cannot be empty")
        
    return search_string