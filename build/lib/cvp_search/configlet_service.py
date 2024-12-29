"""
Business logic for configlet operations
"""
from typing import Dict
from .api_client import CVPApiClient
from .utils.search import filter_configlets

class ConfigletService:
    def __init__(self):
        self.api_client = CVPApiClient()

    def search(self, search_string: str, case_insensitive: bool = False) -> Dict[str, any]:
        """
        Search for configlets and format the results
        
        Args:
            search_string: String to search for in configlets
            case_insensitive: Whether to perform case-insensitive search
            
        Returns:
            Dict containing total count and matching configlets with their data
        """
        response = self.api_client.get_configlets()
        all_configlets = response.get('data', [])
        
        matching_configlets = filter_configlets(
            all_configlets,
            search_string,
            case_insensitive
        )
        
        return {
            'total_count': len(matching_configlets),
            'configlets': matching_configlets
        }