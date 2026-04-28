import os

from art import MOOSE, BAT, ELEPHANT


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def ask_yes_no(prompt: str) -> bool:
    return input(prompt).strip().lower() == "y"


def show_welcome() -> None:
    print("Welcome to the Moose Multiplication Game!")


def get_award(seconds: float) -> str:
    if seconds < 10:
        return BAT
    elif seconds < 20:
        return ELEPHANT
    return MOOSE
