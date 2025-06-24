"""Project brainstorming utilities."""
from .llm import LLMClient


def brainstorm(prompt: str) -> str:
    """Use the LLM to brainstorm project ideas."""
    client = LLMClient()
    seed = (
        "You are an assistant helping to brainstorm software project ideas. "
        "Return a concise list of suggestions."
    )
    full_prompt = f"{seed}\n{prompt}"
    return client.generate(full_prompt)

