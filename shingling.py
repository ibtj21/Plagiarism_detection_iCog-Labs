# shingling.py
# Shingling (breaking a text into small overlapping pieces of words)
# Detects partial plagiarism: Captures copied segments even if only part of the text is reused
# Works efficiently with hashing: Prepares text for rolling hash computation, allowing fast comparison

def generate_shingles(text, k=5):
    """
    Generate k-word shingles from a string.
    Returns a list of shingles (as strings).
    """
    words = text.split()
    shingles = []

    for i in range(len(words) - k + 1): # It slides a window of size k across the list
        shingle = " ".join(words[i:i+k])
        shingles.append(shingle)

    return shingles


def generate_shingles_for_books(preprocessed_books, k=5): 
    # k=5 balances sensitivity(When k is too small,it catches evry small similarity even common expressions ) 
    # and robustness(When k is too large,it catches specific and very large similarities ,dicreases false positives)
    """
    Generate shingles for all preprocessed books.
    preprocessed_books: dict {filename: text}
    Returns dict {filename: list of shingles}
    """
    all_shingles = {}
    for filename, text in preprocessed_books.items():
        shingles = generate_shingles(text, k)
        all_shingles[filename] = shingles
    return all_shingles
# ----------------- function for user input -----------------
def generate_shingles_for_user_text(user_text, k=5):
    """
    Generate k-word shingles from a single user input text.
    Returns a list of shingles.
    """
    return generate_shingles(user_text, k)


