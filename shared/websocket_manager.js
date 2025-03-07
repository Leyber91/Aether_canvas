// Description: A simple WebSocket manager that allows you to connect to a WebSocket server, send messages, and subscribe to events.
// The manager keeps track of subscriptions and calls the appropriate callbacks when a message is received.
// Usage: import { websocketManager } from 'shared/websocket_manager.js';
// websocketManager.connect('ws://localhost:3000');
class WebSocketManager {
    constructor() {
        this.socket = null;
        this.subscriptions = {};
    }

    connect(url, options = {}) {
        this.socket = new WebSocket(url);

        this.socket.onopen = () => {
            console.log('WebSocket connected');
        };

        this.socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            if (this.subscriptions[data.type]) {
                this.subscriptions[data.type].forEach(cb => cb(data.payload));
            }
        };

        this.socket.onerror = (error) => {
            console.error('WebSocket error:', error);
        };

        this.socket.onclose = () => {
            console.log('WebSocket disconnected');
        };
    }

    send(message) {
        if (this.socket.readyState === WebSocket.OPEN) {
            this.socket.send(JSON.stringify(message));
            return true;
        }
        return false;
    }

    subscribe(eventType, callback) {
        const subscriptionId = `sub_${Date.now()}`;
        this.subscriptions[event_type] = this.subscriptions[event_type] || [];
        this.subscriptions[event_type].push({ id: subscriptionId, callback });
        return subscriptionId;
    }

    close() {
        if (this.socket) {
            this.socket.close();
        }
    }
}

export const websocketManager = new WebSocketManager();