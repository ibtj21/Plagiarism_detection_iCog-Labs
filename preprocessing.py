# preprocessing.py

import os
import re

MAX_WORDS = 50000  # ~200 pages

def extract_main_content(text):
    """
    Extracts the main content of a Gutenberg book, removing headers and footers.
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
    text = " ".join(words)

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Remove extra spaces
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
    preprocessed_dir = os.path.join(dataset_dir, "preprocessed")
    os.makedirs(preprocessed_dir, exist_ok=True)

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


