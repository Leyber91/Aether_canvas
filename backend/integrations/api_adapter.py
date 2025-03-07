# backend/integrations/api_adapter.py
import requests
from backend.infrastructure.logger import get_logger
from .api_key_manager import APIKeyManager

logger = get_logger('api_adapter')

class APIAdapter:
    def __init__(self, service_name, base_url):
        self.service_name = service_name
        self.base_url = base_url
        self.api_key_manager = APIKeyManager()

    def execute_request(self, endpoint, method='GET', data=None, params=None, headers=None, stream=False):
        api_key = self.api_key_manager.get_api_key(self.service_name)
        if not api_key:
            logger.error(f"API key not found for service '{self.service_name}'")
            raise ValueError(f"API key not configured for service '{self.service_name}'")

        headers = headers or {}
        headers.update({"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})

        url = f"{self.base_url}{endpoint}"

        try:
            response = requests.request(
                method=method,
                url=url,
                json=data,
                params=params,
                headers=headers,
                stream=stream
            )
            response.raise_for_status()
            return response if stream else response.json()
        except requests.RequestException as e:
            logger.error(f"Error during request to {url}: {e}")
            raise

