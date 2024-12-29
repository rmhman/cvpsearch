"""
Display formatting utilities
"""
from typing import Dict, List

def format_matching_lines(config: str, search_term: str, case_insensitive: bool) -> List[str]:
    """
    Find and format matching lines from configlet content
    
    Args:
        config: Configlet configuration text
        search_term: Search string to match
        case_insensitive: Whether to perform case-insensitive search
        
    Returns:
        List of matching lines, stripped of whitespace
    """
    if not config:
        return []
        
    lines = config.splitlines()
    if case_insensitive:
        search_term = search_term.lower()
        return [line.strip() for line in lines 
                if search_term in line.lower()]
    
    return [line.strip() for line in lines 
            if search_term in line]

def display_results(results: Dict, search_string: str, show_lines: bool = False, 
                   case_insensitive: bool = False) -> None:
    """
    Display search results in a formatted way
    
    Args:
        results: Dictionary containing search results
        search_string: Original search term
        show_lines: Whether to display matching lines
        case_insensitive: Whether search was case-insensitive
    """
    print(f"\nFound {results['total_count']} configlets matching '{search_string}':")
    print("-" * 69)
    
    for configlet in results['configlets']:
        if show_lines:
            print(f"\n{configlet['name']}")
            matching_lines = format_matching_lines(
                configlet.get('config', ''),
                search_string,
                case_insensitive
            )
            for line in matching_lines:
                print(f"  → {line}")
        else:
            print(configlet['name'])
        
    print(f"\nTotal configlets found: {results['total_count']}\n\n")