BLOCKED_KEYWORDS = [
    "bomb", "kill", "harm", "weapon", "violent",
    "overthrow", "extremist", "terror", "suicide",
    "assassinate", "manufacture", "shoot"
]

PROMPT_INJECTION_TRIGGERS = [
    "ignore previous instructions",
    "ignore safety",
    "bypass safety",
    "act as",
    "system override",
    "jailbreak"
]

def check_input_safety(user_input: str) -> tuple[bool, str]:
    """
    Returns (is_safe: bool, message: str)
    """
    lowered = user_input.lower()

    for word in BLOCKED_KEYWORDS:
        if word in lowered:
            return False, f"❌ Unsafe topic detected: '{word}'. I cannot generate a debate on this."

    for inj in PROMPT_INJECTION_TRIGGERS:
        if inj in lowered:
            return False, "❌ Prompt injection attempt detected. Not allowed."

    if len(user_input.strip()) == 0:
        return False, "❌ Input cannot be empty."

    return True, ""
