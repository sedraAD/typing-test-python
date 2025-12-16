"""
Main.py
This program allows users to practice typing using texts of varying 
difficulty levels (easy, medium, hard), and also includes a random character test.
"""

import typing_test
import random_char_test

def main():
    """
    Main function that runs the typing training program.
    It presents the menu to the user and calls the approriate functions based on user input.
    """

    while True:
        print("Menu:")
        print("1) Train easy.")
        print("2) Train medium.")
        print("3) Train hard.")
        print("4) See score list.")
        print("5) Random character typing test.")
        print("q) Quit program.")

        choice = input("Enter choice: ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        if choice == "1":
            typing_test.start_typing_test("./easy.txt", "easy")

        elif choice == "2":
            typing_test.start_typing_test("./medium.txt", "medium")

        elif choice == "3":
            typing_test.start_typing_test("./hard.txt", "hard")

        elif choice == "4":
            typing_test.display_scores("./score.txt")

        elif choice == "5":
            seconds = int(input("Enter number of seconds for the test: "))
            random_char_test.random_character_typing_test(seconds)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        if choice != "q":
            input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
