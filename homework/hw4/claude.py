"""
CSC 251 Homework 4 - Text Analyzer
Author: [Your Name]
Date: [Current Date]
Description: This program analyzes text files to determine various characteristics
including word count, character count, average word/sentence length, unique words,
and frequency of alphabetical and punctuation characters.
"""

import string

# Global constants
SENTENCE_ENDERS = '.?!'
PUNCTUATION_TO_COUNT = '.?!,;:'
WORD_SEPARATORS = string.whitespace

def main():
    """
    Main function to direct the execution of the text analyzer program.
    Prompts for filename, reads text, performs analysis, and outputs results.
    """
    # Get valid filename from user
    filename = get_valid_filename()
    
    # Read text from file
    text = read_file(filename)
    
    # Display the text
    print(f"Text: {text}")
    
    # Perform text analysis
    analyze_text(text)

def get_valid_filename():
    """
    Prompts the user for a filename and validates it exists.
    Continues prompting until a valid filename is entered.
    Returns: Valid filename as a string
    """
    while True:
        try:
            filename = input("Enter filename: ")
            # Try to open the file to check if it exists
            with open(filename, 'r') as f:
                pass
            return filename
        except FileNotFoundError:
            print("File not found. Please enter a valid filename.")
        except Exception as e:
            print(f"Error opening file: {e}. Please try again.")

def read_file(filename):
    """
    Reads all text from the specified file.
    Parameters: filename - name of the file to read
    Returns: String containing all text from the file (without trailing newline)
    """
    try:
        with open(filename, 'r') as f:
            # Read all text and strip the final newline if present
            text = f.read()
            if text.endswith('\n'):
                text = text[:-1]
            return text
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def analyze_text(text):
    """
    Performs comprehensive analysis of the text and outputs results.
    Parameters: text - the text to analyze
    """
    # Extract words and sentences
    words = extract_words(text)
    sentences = count_sentences(text)
    
    # Calculate basic statistics
    total_chars = len(text)
    total_words = len(words)
    
    # Output basic statistics
    print(f"Text contains: {total_words} words, {total_chars} characters")
    
    # Calculate and output average sentence length
    avg_sent_len = avg_sentence_length(text)
    print(f"Average sentence length: {avg_sent_len:.2f} words")
    
    # Calculate and output average word length
    avg_word_len = avg_word_length(words)
    print(f"Average word length: {avg_word_len:.2f} characters")
    
    # Count and output unique words
    unique_count = count_unique_words(words)
    print(f"Number of unique words: {unique_count}")
    
    # Create and output character frequency dictionary
    char_dict = create_dict(text)
    output_dict(char_dict, text)

def extract_words(text):
    """
    Extracts words from text, removing punctuation that isn't part of words.
    Parameters: text - the text to extract words from
    Returns: List of words (preserving case)
    """
    words = []
    current_word = ""
    
    for i, char in enumerate(text):
        if char in WORD_SEPARATORS:
            if current_word:
                # Clean trailing punctuation from word
                current_word = clean_word(current_word, i, text)
                if current_word:
                    words.append(current_word)
                current_word = ""
        else:
            current_word += char
    
    # Don't forget the last word if text doesn't end with whitespace
    if current_word:
        current_word = clean_word(current_word, len(text), text)
        if current_word:
            words.append(current_word)
    
    return words

def clean_word(word, position, text):
    """
    Removes punctuation from the end of a word that shouldn't be part of it.
    Handles special cases like time notation (6:30).
    Parameters: word - the word to clean
                position - position after the word in text
                text - the full text for context
    Returns: Cleaned word
    """
    # Remove trailing punctuation (.,!?;:) unless it's a colon in time notation
    while word and word[-1] in PUNCTUATION_TO_COUNT:
        # Check for time notation (e.g., "6:30")
        if word[-1] == ':' and position < len(text) and not text[position].isspace():
            break
        word = word[:-1]
    
    # Remove trailing double quotes
    while word and word[-1] == '"':
        word = word[:-1]
    
    return word

def count_sentences(text):
    """
    Counts the number of sentences in the text.
    Parameters: text - the text to analyze
    Returns: Number of sentences
    """
    count = 0
    for char in text:
        if char in SENTENCE_ENDERS:
            count += 1
    return count if count > 0 else 1  # At least 1 sentence if there's text

def count_unique_words(words):
    """
    Returns the number of unique words used in the text (case-insensitive).
    Parameters: words - list of words to analyze
    Returns: Count of unique words
    """
    # Use a set for unique words (case-insensitive)
    unique_words = set()
    for word in words:
        unique_words.add(word.lower())
    return len(unique_words)

def avg_word_length(words):
    """
    Returns the average length of words within the text.
    Parameters: words - list of words to analyze
    Returns: Average word length as a float
    """
    if not words:
        return 0.0
    
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def avg_sentence_length(text):
    """
    Returns the average number of words in a sentence within the text.
    Parameters: text - the text to analyze
    Returns: Average sentence length as a float
    """
    words = extract_words(text)
    sentences = count_sentences(text)
    
    if sentences == 0:
        return 0.0
    
    return len(words) / sentences

def create_dict(text):
    """
    Creates a dictionary to hold alphabetical characters and their 
    frequency of occurrence as a key-value pair (case-insensitive).
    Parameters: text - the text to analyze
    Returns: Dictionary with letters as keys and frequencies as values
    """
    char_freq = {}
    
    # Initialize all letters with 0
    for letter in string.ascii_lowercase:
        char_freq[letter] = 0
    
    # Count frequency of each letter (case-insensitive)
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            char_freq[char_lower] += 1
    
    return char_freq

def output_dict(char_dict, text):
    """
    Outputs the dictionary of alphabetical characters with their 
    frequency of occurrence, and also outputs punctuation frequency.
    Parameters: char_dict - dictionary of character frequencies
                text - the original text for punctuation counting
    """
    print("\nFrequency of Characters")
    print("=" * 23)
    print("Letter  Frequency")
    print("-" * 23)
    
    # Output letter frequencies
    for letter in sorted(char_dict.keys()):
        print(f"{letter}       {char_dict[letter]}")
    
    print("-" * 23)
    print("Punctuation  Frequency")
    print("-" * 23)
    
    # Count and output punctuation frequencies
    punct_freq = {}
    for punct in PUNCTUATION_TO_COUNT:
        punct_freq[punct] = text.count(punct)
    
    for punct in PUNCTUATION_TO_COUNT:
        print(f"{punct}            {punct_freq[punct]}")

# Run the main function
if __name__ == "__main__":
    main()