# llm_client.py

import subprocess

def _build_prompt(messages: list[dict]) -> str:
    """
    Convert a list of chat-style messages into a single prompt string
    that can be sent to `ollama run`.
    """
    parts = []
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")

        if role == "system":
            prefix = "System: "
        elif role == "assistant":
            prefix = "Assistant: "
        else:
            prefix = "User: "

        parts.append(prefix + content.strip())

    # End with an assistant cue
    parts.append("Assistant:")
    return "\n\n".join(parts)


def ollama_chat(model: str, messages: list[dict]) -> str:
    """
    Sends a prompt to Ollama using `ollama run` and returns the text output.

    This works on older Ollama versions that do not support `ollama chat`.
    """

    prompt = _build_prompt(messages)

    process = subprocess.Popen(
        ["ollama", "run", model],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    stdout, stderr = process.communicate(prompt)

    if stderr:
        print("Ollama error:", stderr.strip())

    stdout = stdout.strip()
    if not stdout:
        return "⚠️ No response from model."

    return stdout
