# backend/integrations/groq_client.py
import os
import requests
from backend.infrastructure.logger import get_logger

logger = get_logger('groq_client')

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

class GroqClient:

    @staticmethod
    def get_available_models():
        return [
            "llama3-8b-8192",
            "llama3-70b-8192",
            "mixtral-8x7b-32768",
            "gemma2-9b-it",
            "llama-guard-3-8b"
        ]

    @staticmethod
    def chat(model, messages, temperature, max_tokens):
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            logger.error("GROQ_API_KEY not found in environment variables.")
            return {"error": "GROQ_API_KEY not configured"}

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_completion_tokens": max_tokens
        }

        try:
            response = requests.post(GROQ_API_URL, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Chat request to Groq failed: {e}")
            return {"error": str(e)}
