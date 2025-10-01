#!/usr/bin/env python3
"""
mystery_challenge.py

Run: python3 mystery_challenge.py
"""

import base64
import sys

HIDDEN_BASE64 = "aHR0cDovL21lZXQuZ29vZ2xlLmNvbS9oeWUtZ3R6bi1rZnUKVGhpcyBtZWV0aW5nIHdpbGwgYmUgb25seSBnaXJscy4gWW91IGFyZSBob3dldmVyIHdlbGNvbWUgdG8gZW50ZXIgd2l0aCBhIGhpamFiIHNpbmNlIGl0IHdpbGwgYmUgcmVjb3JkZWQu"
# --------------------------------------------------------------------------------------


ANS_PUZZLE1 = "a2liYmxlIGtvbm5lY3Q="  
ANS_PUZZLE2 = "cm9ib3RpY3MgbGFi"      
ANS_PUZZLE3 = "Y2Fycw=="               

def decode_answer(encoded: str) -> str:
    """Decode Base64-encoded answer into plain text (lowercased)."""
    return base64.b64decode(encoded).decode().strip().lower()

def checker(answer: str, expected_encoded: str) -> bool:
    """Normalize and compare the given answer to the hidden Base64-encoded one."""
    if answer is None:
        return False
    expected = decode_answer(expected_encoded)
    return answer.strip().lower() == expected

def prompt_input(prompt_text: str) -> str:
    """Consistent input wrapper (helps if we want to modify behavior later)."""
    try:
        return input(prompt_text)
    except EOFError:
        return ""

def check_with_attempts(prompt_text: str, expected_encoded: str, attempts: int = 2) -> bool:
    """Prompt the user, validate with checker, and allow 'attempts' tries."""
    for attempt in range(1, attempts + 1):
        ans = prompt_input(f"{prompt_text} ")
        if checker(ans, expected_encoded):
            print("Correct.")
            return True
        else:
            if attempt < attempts:
                print("Incorrect. Try again.")
            else:
                print("Incorrect. No attempts left.")
    return False

def puzzle_one():
    print("\nPuzzle 1")
    print("""
    A creation we built to bring pets and their owners together.
    """)
    return check_with_attempts("Enter the secret phrase:", ANS_PUZZLE1, attempts=3)

def puzzle_two():
    print("\nPuzzle 2")
    print("""
    Think of the room where ideas turn into machines that organize and reclaim what’s discarded.
    """)
    return check_with_attempts("Enter the name of the place:", ANS_PUZZLE2, attempts=3)

def puzzle_three():
    print("\nPuzzle 3")
    print("""
    Remember the costumes that brought a race track to life: one was polished and fast, 
    the other bright and playful. Name the story they raced through.
    """)
    return check_with_attempts("Enter the movie title:", ANS_PUZZLE3, attempts=3)

def reveal_link():
    """Decode the HIDDEN_BASE64 and print it to the console."""
    if not HIDDEN_BASE64 or HIDDEN_BASE64.startswith("REPLACE"):
        print("\n[Configuration Error] HIDDEN_BASE64 is not set. Please encode your Drive link and paste it into the script.")
        sys.exit(1)

    try:
        decoded = base64.b64decode(HIDDEN_BASE64).decode().strip()
    except Exception as exc:
        print("\n[Decode Error] Could not decode HIDDEN_BASE64. Check that it's valid Base64.")
        print("Exception:", exc)
        sys.exit(1)

    print("\n🎉 CONGRATULATIONS — you solved the challenge!")
    print("Here is your next hint (Google Meets):")
    print(decoded)
    print("\nProceed with care.")
def main():
    print("=== ACCESS PROTOCOL: PUZZLE CHALLENGE ===")
    print("Solve the puzzles below. Correctly solve all to reveal the next resource.")
    print("Be persistent and patient. Good luck.\n")

    if not puzzle_one():
        print("\nAccess denied. Restart the challenge to try again.")
        return

    if not puzzle_two():
        print("\nAccess denied. Restart the challenge to try again.")
        return

    if not puzzle_three():
        print("\nAccess denied. Restart the challenge to try again.")
        return

    reveal_link()

if __name__ == "__main__":
    main()
