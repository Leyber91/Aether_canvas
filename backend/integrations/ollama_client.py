import requests
import subprocess
from backend.infrastructure.logger import get_logger

logger = get_logger('ollama_client')
OLLAMA_API_URL = "http://localhost:11434/api"

class OllamaClient:
    AVAILABLE_MODELS = [
        "nomic-embed-text:latest",
        "deepseek-r1:8b",
        "deepseek-r1:1.5b",
        "hermes-unleashed-ctx:8b",
        "qwen2.5-coder-extra-ctx:7b",
        "qwen2.5:1.5b",
        "qwen2.5:0.5b",
        "llama3.2:3b",
        "llama3.2:1b"
    ]

    @staticmethod
    def get_available_models():
        try:
            response = requests.get(f"{OLLAMA_API_URL}/tags")
            response.raise_for_status()
            models = response.json().get('models', [])
            return [model['name'] for model in models]
        except requests.RequestException as e:
            logger.error(f"Ollama API error: {e}. Falling back to predefined model list.")
            return OllamaClient.AVAILABLE_MODELS

    @staticmethod
    def chat(model, messages, temperature, max_tokens, stream=False):
        data = {
            "model": model,
            "messages": messages,
            "stream": stream,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens
            }
        }
        logger.info(f"Chat request to Ollama model '{model}' (stream={stream})")
        try:
            response = requests.post(f"{OLLAMA_API_URL}/chat", json=data, stream=stream)
            response.raise_for_status()
            return response.iter_lines() if stream else response.json()
        except requests.RequestException as e:
            logger.error(f"Chat request failed: {e}")
            return {"error": str(e)}
