import random
import time

from ui import get_award, ask_yes_no


def play_round(min_number: int, max_number: int) -> bool:
    """Run one round of the multiplication game."""

    a = random.randint(min_number, max_number)
    b = random.randint(min_number, max_number)
    correct_answer = a * b

    start = time.perf_counter()

    while True:
        guess = input(f"What is {a} * {b}? ").strip().lower()

        if guess == "give up":
            print(f"Correct answer: {correct_answer}")
            break

        try:
            if int(guess) == correct_answer:
                elapsed = time.perf_counter() - start
                print(f"Correct! {round(elapsed, 1)}s")
                print(get_award(elapsed))
                break
        except ValueError:
            pass

        print("Try again or 'give up'.")

    return ask_yes_no("Continue? (y/n): ")
