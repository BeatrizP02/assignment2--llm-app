
import time
from safety import check_input_safety
from llm_client import ollama_chat
from telemetry import log_event
import threading
import itertools
import sys


MODEL = "qwen2.5:1.5b"

SYSTEM_PROMPT = """
You are the Devil's Advocate Debate Generator.
You generate balanced debates using the structure provided by a TOOL.
Follow all rules strictly. Avoid real-world extremist or harmful political persuasion.
"""

def choose_structure(mode: str) -> dict:
    """
    Tool: returns structural rules for generating a debate.
    This satisfies the assignment requirement of tool use.
    """

    if mode != "debate":
        return {
            "sections": [],
            "rules": {
                "tone": "neutral",
                "depth": "short"
            }
        }

    return {
        "sections": [
            "Argument For",
            "Argument Against",
            "Neutral Summary",
            "Discussion Questions"
        ],
        "rules": {
            "tone": "balanced, objective, academic",
            "depth": "moderate detail",
            "safety": "avoid harmful extremist content; avoid real political persuasion"
        }
    }


def generate_debate(topic: str) -> str:
    structure = choose_structure("debate")
    sections = structure["sections"]
    rules = structure["rules"]

    user_prompt = f"""
Topic: {topic}

Please generate a structured debate with the following sections:
{sections}

Rules:
- Tone: {rules['tone']}
- Detail: {rules['depth']}
- Safety: {rules['safety']}
"""

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]

    raw_output = ollama_chat(MODEL, messages)
    numbered_output = raw_output

    for i, section in enumerate(sections, start=1):
        numbered_output = numbered_output.replace(
            f"{section}:",     # replace "Argument For:"
            f"{i}. {section}:"  # with "1. Argument For:"
        )

        numbered_output = numbered_output.replace(
            f"**{section}**",     # replace bold version
            f"**{i}. {section}**"
        )

    return numbered_output

def main():
    print("Devil's Advocate Debate Generator")
    print("Type '/help' for guide.\n")

    while True:
        topic = input("Enter a debate topic: ").strip()

        #Exit
        
        if topic.lower() == "exit":
            print("Goodbye!")
            break
        
        #Help
        if topic.lower() == "/help":
            print(
                "\n=====================================\n"
                "              HELP MENU              \n"
                "=====================================\n"
                "Commands:\n"
                "  /help   - Show this help message\n"
                "  exit    - Quit the application\n"
                "-------------------------------------\n"
                "Just type ANY topic to generate a debate.\n"
                "Example: privacy vs security\n"
                "=====================================\n"
            )
            continue

        # Empty Topic Warning
        if topic == "":
            print("Please enter a valid topic.\n")
            continue

        
        #Safety Check
        safe, msg = check_input_safety(topic)
        if not safe:
            print(msg)
            continue

        #Loading Prompt 
        print("Generating debate... (thinking)\n")

        #Generate Demate
        start = time.time()
        response = generate_debate(topic)
        latency = time.time() - start

        #Log Telemetry
        log_event("tool", latency, len(topic), MODEL)

        print("\n==================== DEBATE ====================\n")
        print(response)
        print("\n=================================================\n")

if __name__ == "__main__":
    main()
