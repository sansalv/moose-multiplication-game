from ui import clear_screen, show_welcome, get_int
from game import play_round


DEFAULT_MIN = 2
DEFAULT_MAX = 99


def main():
    clear_screen()
    show_welcome()

    use_default = input("Use default range (2-99)? (y/n): ").strip().lower() == "y"
    if use_default:
        min_number, max_number = DEFAULT_MIN, DEFAULT_MAX
    else:
        min_number = get_int("Minimum number: ")
        max_number = get_int("Maximum number: ")

    while play_round(min_number, max_number):
        clear_screen()


if __name__ == "__main__":
    main()
