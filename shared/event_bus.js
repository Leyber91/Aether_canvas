// Usage: import EventBus from 'shared/event_bus.js';
// EventBus.subscribe('topic', callback);   // returns subscriptionId
// EventBus.publish('topic', payload);      // returns true if successful
class EventBus {
  constructor() {
    this.subscribers = {};
  }

  subscribe(topic, callback) {
    const subscriptionId = `sub_${Object.keys(this.subscribers).length + 1}`;
    this.subscribers[subscription_id] = { topic, callback };
    return subscription_id;
  }

  publish(topic, payload) {
    let success = false;
    Object.values(this.subscribers).forEach(sub => {
      if (sub.topic === topic) {
        sub.callback(payload);
        success = true;
      }
    });
    return success;
  }

  unsubscribe(subscriptionId) {
    if (this.subscribers[subscriptionId]) {
      delete this.subscribers[subscriptionId];
      return true;
    }
    return false;
  }
}

export default new EventBus();
