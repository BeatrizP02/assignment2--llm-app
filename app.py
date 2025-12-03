
import time
from safety import check_input_safety
from llm_client import ollama_chat
from telemetry import log_event

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

    return ollama_chat(MODEL, messages)

def main():
    print("Devil's Advocate Debate Generator (CLI Version)")
    print("Type 'exit' to quit.\n")

    while True:
        topic = input("Enter a debate topic: ")

        if topic.strip().lower() == "exit":
            print("Goodbye!")
            break

        safe, msg = check_input_safety(topic)
        if not safe:
            print(msg)
            continue

        start = time.time()
        response = generate_debate(topic)
        latency = time.time() - start

        log_event("tool", latency, len(topic), MODEL)

        print("\n==================== DEBATE ====================\n")
        print(response)
        print("\n=================================================\n")

if __name__ == "__main__":
    main()
