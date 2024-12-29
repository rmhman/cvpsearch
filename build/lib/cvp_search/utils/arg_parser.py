"""
Command line argument parsing
"""
import argparse
from typing import NamedTuple

class SearchArgs(NamedTuple):
    search_string: str
    case_insensitive: bool
    show_lines: bool

def parse_args() -> SearchArgs:
    """
    Parse command line arguments
    
    Returns:
        SearchArgs: Named tuple containing search parameters
    """
    parser = argparse.ArgumentParser(description='Search CVP configlets')
    parser.add_argument('search_string', nargs='?', help='String to search for in configlets')
    parser.add_argument('-i', '--ignore-case', action='store_true', 
                       help='Perform case-insensitive search')
    parser.add_argument('-l', '--show-lines', action='store_true',
                       help='Show matching lines from configlets')
    
    args = parser.parse_args()
    return SearchArgs(
        search_string=args.search_string,
        case_insensitive=args.ignore_case,
        show_lines=args.show_lines
    )