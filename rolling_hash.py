# rolling_hash.py

import os

def rolling_hash_shingles(text, k, base=31, mod=10**9+9):
    """
    Compute hashes for all k-shingles using rolling hash.
    text: string
    k: number of characters per shingle
    Returns: list of integer hashes
    """
    n = len(text)
    hashes = []

    if n < k:
        return hashes

    h = 0
    power_k = pow(base, k - 1, mod)

    # First shingle hash
    for i in range(k):
        h = (h * base + ord(text[i])) % mod

    hashes.append(h)

    # Rolling through the rest
    for i in range(1, n - k + 1):
        h = (h - ord(text[i-1]) * power_k) % mod
        h = (h * base + ord(text[i + k - 1])) % mod
        hashes.append(h)

    return hashes


def hash_books_rolling(preprocessed_books, k=5, output_dir="dataset/hashs/"):
    """
    Compute rolling hash for all books and save results.
    preprocessed_books: dict {filename: text}
    k: shingle size (words or characters)
    """
    os.makedirs(output_dir, exist_ok=True)
    hashed_books = {}

    for filename, text in preprocessed_books.items():
        # Convert text to a single string without extra spaces
        text_clean = " ".join(text.split())

        # Compute hashes
        hashes = rolling_hash_shingles(text_clean, k)
        hashed_books[filename] = hashes

        # Save to file
        clean_name = filename.replace(".txt", "_rolling_hashes.txt")
        output_path = os.path.join(output_dir, clean_name)
        with open(output_path, "w", encoding="utf-8") as f:
            for h in hashes:
                f.write(f"{h}\n")

        print(f"Saved rolling hashes for {filename} → {output_path}")

    return hashed_books
# ----------------- function for user input -----------------
def hash_user_text_rolling(user_text, k=5):
    """
    Compute rolling hash for user input text.
    Returns a list of integer hashes.
    """
    # Clean extra spaces
    text_clean = " ".join(user_text.split())
    return rolling_hash_shingles(text_clean, k)