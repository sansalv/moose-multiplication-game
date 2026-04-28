import time
import random
import os


DEFAULT_MIN = 2
DEFAULT_MAX = 99


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def give_award(award: str) -> str:
    """Return the ASCII art award corresponding to the given award name.

    Args:
        award: The award identifier.

    Returns:
        A string containing the matching ASCII art. If the award name is
        unknown, the default moose art is returned.
    """

    moose0 = """
 ___            ___
/   \          /   \ 
\_   \        /  __/ 
 _\   \      /  /__
 \___  \____/   __/ 
     \_       _/ 
       | @ @  \_
       |
     _/     /\ 
    /o)  (o/\ \_
    \_____/ /
      \____/"""

    moose1 = (
        """
You got over 20 seconds.
Here's a moose."""
        + moose0
    )

    bat1 = """
 _______________________________________________________________________
|                                                                       |
|                       You got sub 10 seconds.                         |
|                       Here's your award, a bat.                       |
|        ,*-~"`^"*u_                                _u*"^`"~-*,         |
|     p!^       /  jPw                            w9j \        ^!p      |
|   w^.._      /      "\_                      _/"     \        _.^w    |
|        *_   /          \_      _    _      _/         \     _*        |
|          q /           / \q   ( `--` )   p/ \          \   p          |
|          jj5****._    /    ^\_) o  o (_/^    \    _.****6jj           |
|                   *_ /      "==) ;; (=="      \ _*                    |
|                    `/.w***,   /(    )\   ,***w.\`                     |
|                     ^ ilmk ^c/ )    ( \c^      ^                      |
|                             'V')_)(_('V'                              |
|                                 `` ``                                 |
|_______________________________________________________________________|"""

    elephant1 = """
 _______________________________________
|                                       |
|      You got sub 20 seconds.          |
|   Here is your award, an elephant.    |
|                         ____          |
|                    .---'-    \        |
|       .-----------/           \       |
|      /           (         ^  |   __  |
| &   (             \        O  /  / .' |
| '._/(              '-'  (.   (_.' /   |
|      \                    \     ./    |
|       |    |       |    |/ '._.'      |
|        )   @).____\|  @ |             |
|    .  /    /       (    | mrf         |
|   \|, '_:::\  . ..  '_:::\ ..\).      |
|_______________________________________|"""

    if award == "elephant":
        return elephant1
    elif award == "bat":
        return bat1
    elif award == "moose":
        return moose1
    else:
        return moose0


def main() -> None:
    """Start the multiplication game and manage the overall program flow."""

    clear_screen()
    print("Welcome to the Moose Multiplication Game!")
    print(give_award("moose0"))

    time.sleep(1)
    response = input("\nUse default range (2-99)? (y/n): ").strip().lower()
    should_use_default_range = response == "y"
    if should_use_default_range:
        min_number = DEFAULT_MIN
        max_number = DEFAULT_MAX
    else:
        min_number = get_int("Enter minimum number: ")
        max_number = get_int("Enter maximum number: ")

    does_want_to_play = True
    while does_want_to_play:
        does_want_to_play = play_round(min_number, max_number)

    clear_screen()


def play_round(min_number: int, max_number: int) -> bool:
    """Run one round of the multiplication game.

    Randomly generates two numbers within the given range, prompts the
    player for an answer, and returns whether the player wants to play
    another round.

    Args:
        min_number: The lowest value allowed for generated factors.
        max_number: The highest value allowed for generated factors.

    Returns:
        True if the player chooses to continue, otherwise False.
    """

    clear_screen()

    # Setup the round
    a = random.randint(min_number, max_number)
    b = random.randint(min_number, max_number)
    correct_answer = str(a * b)
    t_init = time.time()

    guess = input(f"What is {a} * {b} ?\n")
    while guess != correct_answer and guess != "give up":
        guess = input(f"\nWrong... Try again or 'give up'\n")
        if guess == "give up":
            break
    if guess == "give up":
        print(f"\nYou gave up.\nThe correct answer was {correct_answer}.")
    else:
        t_end = time.time()
        t = round(t_end - t_init, 1)
        print(f"\nCorrect! Your time was {t} seconds.")
        if t < 10:
            print(give_award("bat"))
        elif t >= 10 and t < 20:
            print(give_award("elephant"))
        else:
            print(give_award("moose"))

    does_want_to_play = input("\nContinue? (y/n)\n") == "y"
    return does_want_to_play


if __name__ == "__main__":
    main()
