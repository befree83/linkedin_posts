"""
Core business logic package initialization.
Exposes OpenAIClient and Chatbot modules to streamline initialization and interactions.
"""

from core.api_client import OpenAIClient
from core.chatbot import Chatbot

__all__ = ["OpenAIClient", "Chatbot"]