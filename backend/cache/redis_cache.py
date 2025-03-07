import redis
import json

class RedisCache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.Redis(host=host, port=port, db=db)

    def get(self, key):
        value = self.client.get(key)
        return json.loads(value) if value else None

    def set(self, key, value, expiry=None):
        self.client.set(key, json.dumps(value), ex=expiry)

    def delete(self, key):
        self.client.delete(key)

    def exists(self, key):
        return self.client.exists(key)

    def flush(self):
        self.client.flushdb()
