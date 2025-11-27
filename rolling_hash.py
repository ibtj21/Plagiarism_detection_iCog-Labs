# rolling_hash.py

import os

def hash_word(word, base=31, mod=10**9+9):
    """
    Convert a single word into an integer hash using a polynomial hash.
    """
    h = 0
    for c in word:
        h = (h * base + ord(c)) % mod
    return h


def rolling_hash_shingles(shingles, base=31, mod=10**9+9):
    """
    Compute rolling hashes for a list of word-level shingles.
    shingles: list of shingles (each shingle = string of k words)
    Returns: list of integer hashes
    """
    if not shingles:
        return []

    # Convert first shingle to list of word hashes
    first_words = shingles[0].split()
    k = len(first_words)
    word_hashes = [hash_word(w, base, mod) for w in first_words]

    # Compute initial hash for first shingle
    h = 0
    for i, wh in enumerate(word_hashes):
        h = (h * base + wh) % mod

    hashes = [h]

    # Precompute base^(k-1) for rolling
    power_k_minus_1 = pow(base, k - 1, mod)

    # Rolling over the rest of the shingles
    for shingle in shingles[1:]:
        words = shingle.split()
        # Remove the hash of the first word of previous shingle
        first_word_hash = hash_word(words[0], base, mod)
        # Compute new hash using rolling formula
        h = (h - word_hashes[0] * power_k_minus_1) % mod
        h = (h * base + hash_word(words[-1], base, mod)) % mod
        hashes.append(h)

        # Update word_hashes for next iteration
        word_hashes = [hash_word(w, base, mod) for w in words]

    return hashes


def hash_books_rolling(shingles_dict, output_dir="dataset/hashes/"):
    """
    Compute rolling hash for all word-level shingles and save results.
    shingles_dict: {filename: [list of shingles]}
    """
    os.makedirs(output_dir, exist_ok=True)
    hashed_books = {}

    for filename, shingles in shingles_dict.items():
        hashes = rolling_hash_shingles(shingles)
        hashed_books[filename] = hashes

        # Save to file
        clean_name = filename.replace(".txt", "_rolling_hashes.txt")
        output_path = os.path.join(output_dir, clean_name)
        with open(output_path, "w", encoding="utf-8") as f:
            for h in hashes:
                f.write(str(h) + "\n")

        print(f"Saved rolling hashes for {filename} → {output_path}")

    return hashed_books


# ---------------- User input hashing ----------------
def hash_user_text_rolling(user_text, k=5):
    """
    Compute rolling hash for USER INPUT text using word-level shingles.
    Returns list of integer hashes.
    """
    from shingling import generate_shingles

    shingles = generate_shingles(user_text, k)
    return rolling_hash_shingles(shingles)
