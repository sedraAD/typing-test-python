"""
typing_test.py
This module contains functions to start typing tests and avaluate user perfomance.
"""

import time
from operator import itemgetter

def read_file(filename):
    """
    Reads a text file and return its content as a list of lines.
    """
    with open(filename, "r", encoding="utf-8") as filehandle:
        return filehandle.readlines()


def calculate_precision(correct, total):
    """
    Calculates precision of typing. For example number of correctly typed words/total words.
    Return the precision percentage rounded to two decimals.
    """
    if total == 0:
        return 100
    return round((correct/total)*100, 2)


def save_score(name, precision, difficulty):
    """
    Saves user's name, precision  and difficulty level in score.txt.
    """
    with open("score.txt", "a", encoding="utf-8") as file_handle:
        file_handle.write(f"\n{name} {precision} {difficulty}")


def show_stats(correct_words, total_words, correct_chars, total_chars, error_count):
    """
    Shows current statistics of the typing test, including word and character precision.
    """
    print("-----------------------------")
    word_precision = calculate_precision(correct_words, total_words)
    char_precision = calculate_precision(correct_chars, total_chars)
    print(f"Ordpresicion: {word_precision}%")
    print(f"teckenpresicion: {char_precision}%")
    print("Felstavade tecken: ")
    if error_count:
        sorted_errors = sorted(error_count.items(), key=itemgetter(1,0), reverse=True)
        for char, count in sorted_errors:
            print(f"{char}: {count}")
    print("-----------------------------")


def correct_words_and_chars(correct_words, correct_chars, error_count, line, user_input):
    """
    Process a single line of the typing test to evaluate the user's input.
    Returns updated counts of correct words and characters.
    """
    line_words = line.split()
    user_words = user_input.split()

    for i, correct_word in enumerate(line_words):
        if i < len(user_words) and correct_word == user_words[i]:
            correct_words += 1
            correct_chars += len(correct_word)
        else:
            if i < len(user_words):
                user_word = user_words[i]
            else:
                user_word = ""
            for j, char in enumerate(correct_word):
                if j < len(user_word):
                    if char == user_word[j]:
                        correct_chars += 1
                    else:
                        error_count[char] = error_count.get(char, 0) + 1
                else:
                    error_count[char] = error_count.get(char, 0) + 1

    return correct_words, correct_chars


def start_typing_test(filename, difficulty):
    """
    Starts the typing test by reading the specified text file and evaluating user input.
    """
    lines = read_file(filename)

    total_words = 0
    total_chars = 0
    correct_words = 0
    correct_chars = 0
    error_count = {}

    start_time = time.time()

    for line in lines:

        show_stats(correct_words, total_words, correct_chars, total_chars, error_count)

        line = line.strip()
        total_words += len(line.split())
        total_chars += len(line.replace(" ", ""))

        print(line)
        user_input = input("")

        correct_words,correct_chars=correct_words_and_chars(correct_words,correct_chars,error_count,line,user_input)

    time_taken = time.time() - start_time

    input("\nPress enter to show result: ")
    show_stats(correct_words, total_words, correct_chars, total_chars, error_count)
    print(f"Det tog {round((time_taken//60))} minuter och {round(time_taken%60, 2)} sekunder.")
    print("-----------------------------")
    word_precision = calculate_precision(correct_words, total_words)

    name = input("Enter name to save results: ")
    save_score(name, word_precision, difficulty)


def display_scores(score_file):
    """
    Dispalys score list from the specified score file.
    """
    try:
        with open(score_file, "r", encoding="utf-8") as file:
            scores = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return
    if not scores:
        print("Inga resultat att visa.")
        return

    score_list = []

    for score in scores:
        parts = score.strip().split()
        if len(parts) < 3:
            continue
        name = parts[0]
        precision = float(parts[1])
        difficulty = parts[2]
        score_list.append((name, precision, difficulty))

    difficulty_order = {"hard": 1, "medium": 2, "easy": 3}
    score_list.sort(key=lambda x: (difficulty_order[x[2]], -x[1]))

    for name, precision, difficulty in score_list:
        print(f"{name} {precision} {difficulty}")
