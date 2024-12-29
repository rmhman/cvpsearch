"""
Search utility functions
"""
from typing import Dict, List

def filter_configlets(
    configlets: List[Dict],
    search_term: str,
    case_insensitive: bool = False
) -> List[Dict]:
    """
    Filter configlets based on search criteria
    
    Args:
        configlets: List of configlet dictionaries
        search_term: String to search for
        case_insensitive: Whether to perform case-insensitive search
        
    Returns:
        List of matching configlet dictionaries
    """
    # Prepare search term based on case sensitivity
    search = search_term.lower() if case_insensitive else search_term
    
    def matches_criteria(configlet: Dict) -> bool:
        name = configlet['name'].lower() if case_insensitive else configlet['name']
        config = configlet.get('config', '')
        if case_insensitive and config:
            config = config.lower()
            
        return search in name or (config and search in config)
    
    return [
        configlet for configlet in configlets
        if matches_criteria(configlet)
    ]