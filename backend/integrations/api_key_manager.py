
# backend/integrations/api_key_manager.py
import os
from cryptography.fernet import Fernet
from backend.infrastructure.logger import get_logger

logger = get_logger('api_key_manager')

class APIKeyManager:
    def __init__(self):
        encryption_key = os.getenv('API_KEYS_ENCRYPTION_KEY')
        if not encryption_key:
            logger.error("API_KEYS_ENCRYPTION_KEY not found in environment variables.")
            raise ValueError("Encryption key not configured")

        self.cipher_suite = Fernet(encryption_key.encode())

    def store_api_key(self, service_name, api_key):
        encrypted_key = self.cipher_suite.encrypt(api_key.encode())
        with open(f"secure_{service_name}_key.bin", "wb") as key_file:
            key_file.write(encrypted_key)
        logger.info(f"API key stored securely for service '{service_name}'.")

    def get_api_key(self, service_name):
        try:
            with open(f"secure_{service_name}_key.bin", "rb") as key_file:
                encrypted_key = key_file.read()
                decrypted_key = self.cipher_suite.decrypt(encrypted_key)
                return decrypted_key.decode()
        except FileNotFoundError:
            logger.error(f"API key file for service '{service_name}' not found.")
            return None
        except Exception as e:
            logger.error(f"Failed to decrypt API key for service '{service_name}': {e}")
            return None

    def rotate_api_key(self, service_name, new_api_key):
        self.store_api_key(service_name, new_api_key)
        logger.info(f"API key rotated successfully for service '{service_name}'.")
