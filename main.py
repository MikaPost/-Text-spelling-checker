"""
This file is for our new theme: Text spelling checker
Created by: Miqayel Postoyan
Date: 28 June
"""

import argparse
from spellchecker import SpellChecker


def get_arguments():
    """
    Function: get_arguments
    Brief: Parses command line arguments to get input and output file paths.
    Params: None
    Return: fname (str): Input file path
            output (str): Output file path
    """
    parser = argparse.ArgumentParser(description="Check and correct text spelling mistakes.")
    parser.add_argument("-f", "--file", required=True, help="Input file")
    parser.add_argument("-o", "--output", required=True, help="Output file")

    args = parser.parse_args()

    fname = args.file
    output = args.output

    return fname, output


def correct_spelling(input_file, output_file):
    """
    Function: correct_spelling
    Brief: Checks and corrects spelling mistakes in the input file.
    Params: input_file (str): Path to the input file
            output_file (str): Path to the output file
    Return: None
    """
    spell = SpellChecker()

    with open(input_file, 'r') as file:
        text = file.read()

    words = text.split()
    corrected_text = []

    for word in words:
        if word not in spell:
            suggestions = spell.candidates(word)
            print(suggestions)
            if suggestions:
                print(f"The word '{word}' is misspelled.")
                print("Suggestions:")
                for i, suggestion in enumerate(suggestions, 1):
                    print(f"{i}. {suggestion}")

                choice = int(input("Choose the correct word (number): ")) - 1
                corrected_word = list(suggestions)[choice]
            else:
                print(f"No suggestions found for '{word}'. Keeping the original.")
                corrected_word = word
        else:
            corrected_word = word

        corrected_text.append(corrected_word)

    with open(output_file, 'w') as file:
        file.write(' '.join(corrected_text))


def main():
    """
    Function: main
    Brief: Entry point of the program. Gets file paths and calls correct_spelling function.
    Params: None
    Return: None
    """
    file, output = get_arguments()

    correct_spelling(file, output)


if __name__ == "__main__":
    main()
