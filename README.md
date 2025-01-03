# CVP Configlet Search Tool

A Python-based command-line tool for searching Arista's CloudVision Portal (CVP) configlets.

## Overview

This tool allows you to search for configlets in CVP using a search string and displays the matching configlet names along with their matching lines. It uses the CVP API and requires an API key for authentication.

## Prerequisites

- Python 3.6 or higher
- CVP API key (stored in environment variable `CVP_KEY`)
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your CVP API key as an environment variable:

   ```bash
   export CVP_KEY='your-api-key-here'
   ```

## Project Structure

```bash
.
├── README.md
├── requirements.txt
├── cvp_search.py
└── src/
    └── cvp_search/
        ├── __init__.py
        ├── main.py
        ├── api_client.py
        ├── configlet_service.py
        ├── constants.py
        ├── exceptions.py
        └── utils/
            ├── __init__.py
            ├── arg_parser.py
            ├── display.py
            ├── input_handler.py
            └── search.py
```

### Module Descriptions

- `cvp_search.py`: Entry point script
- `src/cvp_search/`:
  - `main.py`: Main application logic and error handling
  - `api_client.py`: CVP API communication handler
  - `configlet_service.py`: Business logic for configlet operations
  - `constants.py`: Application-wide constants (API endpoints, defaults)
  - `exceptions.py`: Custom exception classes
  - `utils/`:
    - `arg_parser.py`: Command line argument parsing
    - `display.py`: Result formatting and display logic
    - `input_handler.py`: Input validation and handling
    - `search.py`: Search and filtering utilities

## Usage

Run the script with various options:

```bash
# Basic search
python cvp_search.py "<search-string>"

# Case-insensitive search
python cvp_search.py -i "<search-string>"
python cvp_search.py --ignore-case "<search-string>"

# Show matching lines
python cvp_search.py -l "<search-string>"
python cvp_search.py --show-lines "<search-string>"

# Combine options
python cvp_search.py -i -l "<search-string>"

# Without argument - will prompt for search string
python cvp_search.py
```

Example outputs:

```bash
# Basic search
$ python cvp_search.py "VLAN"
Found 3 configlets matching 'VLAN':
--------------------------------------------------

spine01-base
leaf01-base
leaf02-base

Total configlets found: 3

# Search with line display
$ python cvp_search.py -l "VLAN"
Found 3 configlets matching 'VLAN':
--------------------------------------------------

spine01-base
  → vlan 100
  → vlan 200

leaf01-base
  → vlan 100
  → vlan access 100

leaf02-base
  → vlan 200
  → vlan trunk allowed 200

Total configlets found: 3
```

## Error Handling

The tool handles various error scenarios:

- Missing API key (`APIKeyError`)
- Invalid API responses
- Network connectivity issues
- Empty search strings
- Invalid command-line arguments

## Security Notes

- SSL certificate verification is disabled for internal corporate environments
- API key is stored as an environment variable for security
- Warning messages for insecure requests are suppressed

## Dependencies

- requests>=2.31.0
- urllib3>=2.0.0

## Contributing

1. Follow the existing code structure:
   - Keep files small and focused
   - Each module has a single responsibility
   - Use appropriate error handling
   - Maintain consistent code style
2. Include type hints for all functions
3. Add docstrings for all modules, classes, and functions
4. Update documentation as needed
5. Follow PEP 8 style guidelines
