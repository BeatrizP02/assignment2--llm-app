
import json
from app import generate_debate
from safety import check_input_safety

def run_test(test: dict) -> bool:
    topic = test["input"]

    # Safety first
    safe, msg = check_input_safety(topic)

    if test.get("expect_refusal"):
        return not safe

    if not safe:
        return False

    # Generate debate
    output = generate_debate(topic)

    # Check expected sections
    if "expected_sections" in test:
        for section in test["expected_sections"]:
            if section.lower() not in output.lower():
                return False

    # Check expected content
    if "expected_contains_any" in test:
        if not any(word.lower() in output.lower() for word in test["expected_contains_any"]):
            return False

    # Check minimum output length
    if "expected_min_chars" in test:
        if len(output) < test["expected_min_chars"]:
            return False

    return True


def main():
    with open("tests.json", "r", encoding="utf-8") as f:
        tests = json.load(f)

    total = len(tests)
    passed = 0

    print(">Running Offline Evaluation...\n")

    for test in tests:
        result = run_test(test)
        if result:
            passed += 1
        print(f"- {test['name']}: {'PASS' if result else 'FAIL'}")

    print("\n======================================")
    print(f"PASS RATE: {passed}/{total}  ({(passed/total)*100:.1f}%)")
    print("======================================\n")


if __name__ == "__main__":
    main()
