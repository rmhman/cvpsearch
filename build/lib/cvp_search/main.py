"""
Main application logic
"""
import sys
from .configlet_service import ConfigletService
from .utils.arg_parser import parse_args
from .utils.input_handler import get_search_string
from .utils.display import display_results
from .exceptions import APIKeyError

def main():
    try:
        # Parse command line arguments
        args = parse_args()
        
        # Get search string from either command line or prompt
        search_string = get_search_string(args.search_string)
        
        # Perform the search
        service = ConfigletService()
        results = service.search(search_string, case_insensitive=args.case_insensitive)
        
        # Display results
        display_results(
            results,
            search_string,
            show_lines=args.show_lines,
            case_insensitive=args.case_insensitive
        )
        
    except APIKeyError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()