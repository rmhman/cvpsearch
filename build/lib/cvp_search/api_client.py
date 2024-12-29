"""
CVP API client implementation
"""
import os
import requests
import urllib3
from typing import Dict
from .constants import API_ENDPOINTS, DEFAULT_LIMIT
from .exceptions import APIKeyError

# Suppress InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class CVPApiClient:
    def __init__(self):
        self.api_key = self._get_api_key()
        self.base_url = "https://usvad001cvpsr01a.corp.internal.citizensbank.com/cvpservice"
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Accept': 'application/json',
        }

    def _get_api_key(self) -> str:
        """Retrieve API key from environment variable"""
        api_key = os.getenv('CVP_KEY')
        if not api_key:
            raise APIKeyError("CVP_KEY environment variable is not set")
        return api_key

    def get_configlets(self, limit: int = DEFAULT_LIMIT) -> Dict:
        """
        Get all configlets from CVP
        
        Args:
            limit: Maximum number of configlets to retrieve
            
        Returns:
            Dict containing configlets data
        """
        endpoint = f"{self.base_url}{API_ENDPOINTS['GET_CONFIGLETS']}"
        params = {
            'type': 'Configlet',
            'startIndex': 0,
            'endIndex': limit
        }

        response = requests.get(
            endpoint,
            headers=self.headers,
            params=params,
            verify=False
        )
        response.raise_for_status()
        
        return response.json()