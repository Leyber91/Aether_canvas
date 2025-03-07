### shared/websocket_manager.py

import asyncio
import websockets

class WebSocketManager:
    def __init__(self):
        self.clients = {}
        self.handlers = {}

    def register_handler(self, event_type, handler):
        self.handlers[event_type] = handler

    async def handle_connection(self, websocket, path):
        client_id = id(websocket)
        self.clients[client_id] = websocket
        try:
            async for message in websocket:
                await self.process_message(client_id, message)
        finally:
            del self.clients[client_id]

    async def process_message(self, client_id, message):
        data = json.loads(message)
        event_type = data.get('type')
        payload = data.get('payload')
        if handler := self.handlers.get(event_type):
            await handler(client_id, payload)

    async def broadcast(self, event_type, payload):
        message = json.dumps({'type': event_type, 'payload': payload})
        await asyncio.wait([client.send(message) for client in self.clients.values()])

    async def send_to_client(self, client_id, payload):
        if client := self.clients.get(client_id):
            await client.send(json.dumps(payload))

websocket_manager = WebSocketManager()