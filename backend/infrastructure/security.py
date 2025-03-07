import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'your-secure-secret-key'

class Security:
    @staticmethod
    def generate_api_key(user_id, expiry_days=30):
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(days=expiry_days)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    @staticmethod
    def validate_api_key(api_key):
        try:
            payload = jwt.decode(api_key, SECRET_KEY, algorithms=['HS256'])
            return True, payload
        except jwt.ExpiredSignatureError:
            return False, 'API key expired'
        except jwt.InvalidTokenError:
            return False, 'Invalid API key'
