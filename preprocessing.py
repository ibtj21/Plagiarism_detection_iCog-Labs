# preprocessing.py

import os #for working with files and folders:to check if sth is in foldeer,to create new folder etc
import re #for text pattern cleaning using regular expressions.Like removing extra spaces and punctuation

MAX_WORDS = 50000  # ~200 pages

def extract_main_content(text):
    """
    Extracts the main content of a Gutenberg book, removing headers and footers.
    Finds and removes everything before and after the real book content.
    """
    start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
    end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"

    # Find start
    start_idx = text.find(start_marker)
    if start_idx != -1:
        text = text[start_idx + len(start_marker):]

    # Find end
    end_idx = text.find(end_marker)
    if end_idx != -1:
        text = text[:end_idx]

    return text.strip()


def clean_text(text, max_words=MAX_WORDS):
    """
    Preprocess the text:
    - Keep only main content
    - Chop to max_words
    - Lowercase
    - Remove punctuation
    - Remove extra spaces
    """
    text = extract_main_content(text)

    # Chop to max_words
    words = text.split()
    if len(words) > max_words:
        words = words[:max_words]
    text = " ".join(words)  #Take a list of words and combine them into one string with spaces between them

    # Lowercase
    text = text.lower() 

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text) # Remove anything that is NOT a letter, NOT a number, and NOT a space
                                        #\w	: Any letter or number (a–z, A–Z, 0–9, or _) , \s	Any space or whitespace , ^ :NOT

    # Remove extra spaces and replace with single space
    text = re.sub(r'\s+', ' ', text).strip() 
 
    return text


def preprocess_dataset(dataset_dir="dataset/"):
    """
    Preprocess all .txt books in the dataset directory.
    Returns a dictionary: {filename: preprocessed_text}
    Also saves each preprocessed book in dataset/preprocessed/
    """
    preprocessed_books = {}

    # Create preprocessed folder if it doesn't exist
    preprocessed_dir = os.path.join(dataset_dir, "preprocessed") #dataset_dir = "dataset/"
    os.makedirs(preprocessed_dir, exist_ok=True) # preprocessed_dir = "dataset/preprocessed"

    for filename in os.listdir(dataset_dir):
        file_path = os.path.join(dataset_dir, filename)

        # Only process text files, skip folders
        if os.path.isfile(file_path) and filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                cleaned_text = clean_text(text)
                preprocessed_books[filename] = cleaned_text

                # Save preprocessed text
                output_filename = filename.replace(".txt", "_clean.txt")
                output_path = os.path.join(preprocessed_dir, output_filename)
                with open(output_path, "w", encoding="utf-8") as out_f:
                    out_f.write(cleaned_text)

                print(f"Saved preprocessed file: {output_path}")  # confirmation

    return preprocessed_books

# ----------------- function for user input -----------------
def preprocess_user_text(text, max_words=MAX_WORDS):
    """
    Preprocesses user input text: # same as clean_text but not extracting main content.
    - Lowercase
    - Remove punctuation
    - Remove extra spaces
    - Chop to max_words
    """
    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Chop to max_words
    words = text.split()
    if len(words) > max_words:
        words = words[:max_words]
    text = " ".join(words)

    return text

