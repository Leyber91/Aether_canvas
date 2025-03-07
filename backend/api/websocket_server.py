# backend/api/websocket_server.py
import asyncio
import json
import traceback
from websockets import serve, exceptions
from backend.infrastructure.logger import get_logger
from backend.infrastructure.security import Security

logger = get_logger('websocket_server')

connected_clients = {}

async def handle_client(websocket, path):
    client_id = None
    try:
        # Wait for authentication message
        auth_message = await websocket.recv()
        try:
            auth_data = json.loads(auth_message)
        except json.JSONDecodeError:
            logger.warning("Invalid JSON in WebSocket authentication message")
            await websocket.send(json.dumps({"error": "Invalid authentication format"}))
            return
        
        # Check for API key (in a real system, validate this properly)
        if 'api_key' not in auth_data:
            logger.warning("Missing API key in WebSocket authentication")
            await websocket.send(json.dumps({"error": "Authentication failed: missing API key"}))
            return
        
        # Get client ID or generate one
        client_id = auth_data.get('client_id', f"anonymous_{id(websocket)}")
        connected_clients[client_id] = websocket
        logger.info(f"Client '{client_id}' connected successfully")
        
        # Send confirmation
        await websocket.send(json.dumps({"type": "connected", "client_id": client_id}))
        
        # Message handling loop
        async for message in websocket:
            try:
                await process_message(client_id, message, websocket)
            except Exception as e:
                error_msg = f"Error processing message from client {client_id}: {str(e)}"
                logger.error(error_msg)
                await websocket.send(json.dumps({"error": error_msg}))
    
    except exceptions.ConnectionClosed:
        logger.info(f"Connection with client '{client_id}' closed")
    except Exception as e:
        error_msg = f"Unexpected error in WebSocket connection: {str(e)}"
        logger.error(error_msg)
        logger.debug(traceback.format_exc())
        
        # Try to send error message if connection is still open
        if websocket.open:
            try:
                await websocket.send(json.dumps({"error": error_msg}))
            except:
                pass
    finally:
        # Clean up client connection
        if client_id:
            connected_clients.pop(client_id, None)
            logger.info(f"Client '{client_id}' disconnected")

async def process_message(client_id, message, websocket):
    """Process an incoming WebSocket message"""
    try:
        data = json.loads(message)
    except json.JSONDecodeError:
        await websocket.send(json.dumps({"error": "Invalid JSON message"}))
        return
    
    message_type = data.get('type')
    
    # Handle different message types
    if message_type == 'ping':
        await websocket.send(json.dumps({"type": "pong"}))
    elif message_type == 'echo':
        await websocket.send(json.dumps({"type": "echo", "message": data.get('message', '')}))
    else:
        logger.warning(f"Unknown message type: {message_type}")
        await websocket.send(json.dumps({"error": f"Unknown message type: {message_type}"}))

async def send_to_client(client_id, message):
    """Send a message to a specific client"""
    websocket = connected_clients.get(client_id)
    if websocket and websocket.open:
        try:
            await websocket.send(json.dumps(message))
            return True
        except Exception as e:
            logger.error(f"Error sending message to client {client_id}: {e}")
    return False

async def broadcast(message):
    """Broadcast a message to all connected clients"""
    if not connected_clients:
        return
    
    # Create tasks for sending to each client
    send_tasks = [
        send_to_client(client_id, message) 
        for client_id in connected_clients
    ]
    
    # Execute all tasks and collect results
    results = await asyncio.gather(*send_tasks, return_exceptions=True)
    
    # Log any errors
    for client_id, result in zip(connected_clients.keys(), results):
        if isinstance(result, Exception):
            logger.error(f"Error broadcasting to client {client_id}: {result}")

async def main():
    """Start the WebSocket server"""
    try:
        async with serve(handle_client, "0.0.0.0", 6789):
            logger.info("WebSocket server started at ws://0.0.0.0:6789")
            await asyncio.Future()  # Run forever
    except Exception as e:
        logger.error(f"WebSocket server error: {e}")

if __name__ == '__main__':
    asyncio.run(main())