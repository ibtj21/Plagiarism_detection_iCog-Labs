# shingling.py

def generate_shingles(text, k=5):
    """
    Generate k-word shingles from a string.
    Returns a list of shingles (as strings).
    """
    words = text.split()
    shingles = []

    for i in range(len(words) - k + 1):
        shingle = " ".join(words[i:i+k])
        shingles.append(shingle)

    return shingles


def generate_shingles_for_books(preprocessed_books, k=5):
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


# # Example usage
# if __name__ == "__main__":
#     from preprocessing import preprocess_dataset
#     dataset_dir = "dataset/preprocessed"
#     books = preprocess_dataset(dataset_dir)

#     k = 5  # 5-word shingles
#     shingles_dict = generate_shingles_for_books(books, k)

#     for name, shingles in shingles_dict.items():
#         print(f"{name}: {len(shingles)} shingles")
