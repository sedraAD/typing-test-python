"""
random_char_test.py
This module contains the function to run a random character typing test for a specified time.
"""

import time
import random
from operator import itemgetter

def display_result(correct_characters, total_errors, seconds):
    """
    Display the result of the random character typing test after it finishes.
    """
    total_typed = correct_characters + total_errors
    if total_typed > 0:
        error_percentage = round((total_errors/total_typed)*100, 2)
    else:
        error_percentage = 0.0
    cpm = round((total_typed/(seconds/60)), 2)

    print("\nTimes's up")
    print(f"Total characters typed: {total_typed}")
    print(f"Error percentage: {error_percentage}%")
    print(f"Characters per minute: {cpm}")


def random_character_typing_test(seconds):
    """
    Runs a random character typing test for a specified number of seconds.
    """
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    correct_characters = []
    error_count = {}

    print(f"type as many characters as you can in {seconds} seconds!")

    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        random_char = random.choice(characters)
        print(random_char)
        user_input = input("")

        if user_input != random_char:
            error_count[random_char] = error_count.get(random_char, 0) + 1
        else:
            correct_characters.append(user_input)

    total_characters = len(correct_characters)
    total_errors = sum(error_count.values())

    display_result(total_characters, total_errors, seconds)

    if error_count:
        print("Errors:")
        sorted_errors = sorted(error_count.items(), key=itemgetter(1,0), reverse=True)
        for char, count in sorted_errors:
            print(f"{char}: {count}")
    else:
        print("No errors!")
