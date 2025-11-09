"""
Author: Frank Lin
Email: fclin@ncsu.edu
Class: CSC 251 Fall 2025
Program: Homework 4
Purpose: Analyzes a text file for writing style.
Bugs: None
Acknowledgements: Used Claude AI to help with output_dict() function. 
Also used it to refactor project for cleaner structure.
"""

import string
from header import header

# Globals
ENDERS = '.?!'
PUNCTUATION = '.?!,;:'
SEPARATORS = string.whitespace

def main():
    """
    Main function to direct the execution of the program.
    """
    # Get valid filename and read text
    text = read_file()

    # Display text
    display_text = ""
    if text.endswith('\n'):
        display_text = text[:-1] 
    else:
        display_text = text
    print(f"Text: {display_text}\n")

    # Perform text analysis
    words = extract_words(text)
    sentence_count = count_sentences(text)

    num_chars = len(text)  
    num_words = len(words)

    # Output results
    print(f"Text contains: {num_words} words, {num_chars} characters")

    avg_sent_len = avg_sentence_length(text)
    print(f"Average sentence length: {avg_sent_len:.2f} words")

    avg_word_len = avg_word_length(words)
    print(f"Average word length: {avg_word_len:.2f} characters")

    unique_count = count_unique_words(words)
    print(f"Number of unique words: {unique_count}")

    char_dict = create_dict(text)
    output_dict(char_dict, text)

def read_file():
    """
    Prompts user for a filename and reads all text from the file.
    Parameters: filename - str
    Returns: string containing all text from the file
    """
    valid = False
    filename = ""

    # Check for valid filename
    while not valid:
        try:
            filename = input("Enter filename: ")
            with open(filename, 'r') as f:
                pass
            valid = True
        except FileNotFoundError:
            print("File not found. Please enter a valid filename.")
        except Exception as e:
            print(f"Error opening file: {e}. Please try again.")

    # Read text from file
    try:
        with open(filename, 'r') as f:
            text = f.read()
            return text
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def extract_words(text):
    """
    Extracts words from text, removing punctuation that isn't part of words.
    Parameters: text - the text to extract words from
    Returns: List of words (preserving case)
    """
    words = []
    current_word = ""
    i = 0
    
    for char in text:
        if char in SEPARATORS:
            if current_word:
                # Clean trailing punctuation from word
                current_word = clean_word(current_word, i, text)
                if current_word:
                    words.append(current_word)
                current_word = ""
        else:
            current_word += char
        i += 1  # advance index
    
    # If text doesn't end with whitespace, add the last word
    if current_word:
        current_word = clean_word(current_word, len(text), text)
        if current_word:
            words.append(current_word)
    
    return words

def clean_word(word, position, text):
    """
    Removes punctuation from the end of a word that shouldn't be part of it.
    Handles special cases like time notation.
    Parameters:
        word     - str
        position - int
        text     - str
    Returns: Cleaned word
    """
    # Remove leading double quotes
    while word and word[0] == '"':
        word = word[1:]
    
    # Remove trailing punctuation and quotes
    while word:
        last_char = word[-1]

        # Handle time notation
        if last_char == ":" and position < len(text) and not text[position].isspace():
            break

        # Strip punctuation
        if last_char in PUNCTUATION or last_char == '"':
            word = word[:-1]
        else:
            break

    return word

def count_sentences(text):
    """
    Counts the number of sentences in the text.
    Parameters: text - the text to analyze
    Returns: Number of sentences
    """
    count = 0
    for char in text:
        if char in ENDERS:
            count += 1
    if count > 0:
        return count
    else:
        return 1  # At least 1 sentence if there's text

def count_unique_words(words):
    """
    Returns the number of unique words.
    Parameters: words - list
    Return: count of unique words - int
    """
    unique_words = set()  # Start with empty set
    for word in words:
        unique_words.add(word.lower())  # Only add lowercase version
    count = len(unique_words)
    return count

def avg_word_length(words):
    """
    Returns the average word length.
    Parameters: words - list
    Return: average word length - float
    """
    total_length = 0
    for word in words:
        total_length += len(word)
    avg_length = 0
    if len(words) > 0: # only divide if list is not empty
        avg_length = total_length / len(words)
    return avg_length

def avg_sentence_length(text):
    """
    Returns the average number of words per sentence in the text.
    Parameters: text - str
    Returns: float
    """
    num_sentences = count_sentences(text)
    words = extract_words(text)
    if num_sentences > 0:
        return len(words) / num_sentences
    return 0

def create_dict(text):
    """
    Creates a dictionary to hold alphabetical characters 
    and their frequency of occurrence as a key-value pair.
    """
    char_dict = {}
    for letter in string.ascii_lowercase:
        char_dict[letter] = 0

    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            char_dict[char_lower] += 1
    
    return char_dict


def output_dict(char_dict, text):
    """
    Outputs the dictionary of alphabetical characters with their frequency of 
    occurrence.
    """     
    header()

    # Output letter frequencies
    for letter in sorted(char_dict.keys()):
        print(f"{letter:>5}        {char_dict[letter]:>5}")
    
    print("-" * 23)
    print(f"{'Punctuation':<12} {'Frequency'}")
    print("-" * 23)
    
    # Count and output punctuation frequencies
    punct_freq = {punct: text.count(punct) for punct in PUNCTUATION}
    
    for punct in PUNCTUATION:
        print(f"{punct:>5}        {punct_freq[punct]:>5}")

if __name__ == "__main__":
    main()