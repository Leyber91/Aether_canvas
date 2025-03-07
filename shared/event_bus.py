# shared/event_bus.py

from collections import defaultdict
from uuid import uuid4

class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, topic, callback):
        subscription_id = f"sub_{len(self.subscribers)+1}"
        self.subscribers[subscription_id] = {'topic': topic, 'callback': callback}
        return subscription_id

    def publish(self, topic, payload):
        success = False
        for sub in self.subscribers.values():
            if sub['topic'] == topic:
                sub['callback'](payload)
                success = True
        return success

    def unsubscribe(self, subscription_id):
        return self.subscribers.pop(subscription_id, None) is not None
