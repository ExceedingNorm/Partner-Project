"""LLM integration for Partner app.
This module provides a simple wrapper around a generic Large Language Model API.
Users must supply API credentials and configuration via environment variables or
function parameters.
"""
from dataclasses import dataclass
from typing import Optional, Dict, Any
import os
import requests


@dataclass
class LLMConfig:
    """Configuration for connecting to the LLM."""
    api_key: str
    endpoint: str
    model: str


class LLMClient:
    """Simple client to interact with an LLM via HTTP."""

    def __init__(self, config: Optional[LLMConfig] = None) -> None:
        if config is None:
            config = LLMConfig(
                api_key=os.getenv("LLM_API_KEY", ""),
                endpoint=os.getenv("LLM_ENDPOINT", ""),
                model=os.getenv("LLM_MODEL", ""),
            )
        self.config = config

    def generate(self, prompt: str, **params: Any) -> str:
        """Send a prompt to the LLM and return the generated text."""
        headers = {"Authorization": f"Bearer {self.config.api_key}"}
        payload: Dict[str, Any] = {"prompt": prompt, "model": self.config.model}
        payload.update(params)
        response = requests.post(self.config.endpoint, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get("choices", [{}])[0].get("text", "")

