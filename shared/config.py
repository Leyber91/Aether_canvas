import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env', override=True)  # Explicit reload

class ConfigManager:
    def __init__(self):
        self.config = {
            'ENVIRONMENT': os.getenv('ENVIRONMENT', 'development'),
            'DATABASE_URL': os.getenv('DATABASE_URL'),
            'REDIS_URL': os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
            'DEBUG_MODE': os.getenv('DEBUG_MODE', 'true').lower() == 'true'
        }

    def get_config(self, key, default_value=None):
        return self.config.get(key, default_value)

config = ConfigManager()
