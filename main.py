# import sys
# sys.stdout.reconfigure(encoding="utf-8")

# from preprocessing import preprocess_dataset
# from shingling import generate_shingles_for_books
# from rolling_hash import hash_books_rolling  # updated rolling hash function
# import os

# def main():
#     dataset_dir = "dataset/"

#     # 1️⃣ Preprocess all books
#     books = preprocess_dataset(dataset_dir)

#     for name, text in books.items():
#         print(f"{name}: {len(text.split())} words")

#     preprocessed_dir = os.path.join(dataset_dir, "preprocessed")
#     print(f"Preprocessed books saved in '{preprocessed_dir}'")

#     # 2️⃣ Generate shingles
#     shingles_dict = generate_shingles_for_books(books, k=5)

#     # 3️⃣ Save shingles into dataset/shingles/
#     shingles_dir = os.path.join(dataset_dir, "shingles")
#     os.makedirs(shingles_dir, exist_ok=True)

#     for name, shingles in shingles_dict.items():
#         output_path = os.path.join(shingles_dir, name.replace(".txt", "_shingles.txt"))
#         with open(output_path, "w", encoding="utf-8") as f:
#             for shingle in shingles:
#                 f.write(shingle + "\n")
#         print(f"Shingles saved for {name} -> {output_path}")

#     print(f"All shingles saved in '{shingles_dir}'")

#     # 4️⃣ Compute rolling hashes for each book and save
#     print("\nComputing rolling hashes for all books...")
#     hashes_dir = os.path.join(dataset_dir, "hashs")
#     hashed_books = hash_books_rolling(books, k=5, output_dir=hashes_dir)

#     print(f"All rolling hashes saved in '{hashes_dir}'")

# if __name__ == "__main__":
#     main()


# import sys
# sys.stdout.reconfigure(encoding="utf-8")

# from preprocessing import preprocess_dataset
# from shingling import generate_shingles_for_books
# from rolling_hash import hash_books_rolling  # updated rolling hash function
# from trie_autocomplete import trie_insert, autocomplete
# import os

# # ---------------- Helper: Build trie from preprocessed books ----------------
# def build_trie_from_books(preprocessed_books):
#     """
#     Build a trie containing all words from preprocessed books
#     """
#     root = [None]  # root as list to mimic pointer behavior
#     for text in preprocessed_books.values():
#         words = text.split()
#         for word in words:
#             trie_insert(root, word)
#     return root

# # ---------------- Main ----------------
# def main():
#     dataset_dir = "dataset/"

#     # 1️⃣ Preprocess all books
#     books = preprocess_dataset(dataset_dir)

#     for name, text in books.items():
#         print(f"{name}: {len(text.split())} words")

#     preprocessed_dir = os.path.join(dataset_dir, "preprocessed")
#     print(f"Preprocessed books saved in '{preprocessed_dir}'")

#     # 2️⃣ Generate shingles
#     shingles_dict = generate_shingles_for_books(books, k=5)

#     # 3️⃣ Save shingles into dataset/shingles/
#     shingles_dir = os.path.join(dataset_dir, "shingles")
#     os.makedirs(shingles_dir, exist_ok=True)

#     for name, shingles in shingles_dict.items():
#         output_path = os.path.join(shingles_dir, name.replace(".txt", "_shingles.txt"))
#         with open(output_path, "w", encoding="utf-8") as f:
#             for shingle in shingles:
#                 f.write(shingle + "\n")
#         print(f"Shingles saved for {name} -> {output_path}")

#     print(f"All shingles saved in '{shingles_dir}'")

#     # 4️⃣ Compute rolling hashes for each book and save
#     print("\nComputing rolling hashes for all books...")
#     hashes_dir = os.path.join(dataset_dir, "hashs")
#     hashed_books = hash_books_rolling(books, k=5, output_dir=hashes_dir)
#     print(f"All rolling hashes saved in '{hashes_dir}'")

#     # 5️⃣ Build trie for autocomplete
#     print("\nBuilding trie for autocomplete...")
#     trie_root = build_trie_from_books(books)
#     print("✅ Trie built successfully from preprocessed books")

#     # # 6️⃣ User input with autocomplete
#     # while True:
#     #     prefix = input("\nType a prefix for autocomplete (or 'quit' to exit): ").strip()
#     #     if prefix.lower() == "quit":
#     #         break
#     #     suggestions = autocomplete(trie_root, prefix)
#     #     print(f"Autocomplete suggestions: {suggestions[:10]}")  # show first 10
#     # ---------------- 6️⃣ User input with autocomplete ----------------
#     print("\nType a prefix to get autocomplete suggestions (or 'quit' to exit):")

#     while True:
#         prefix = input("Prefix: ").strip()
#         if prefix.lower() == "quit":
#             break
#         # Get suggestions from trie
#         suggestions = autocomplete(trie_root, prefix)
#         if suggestions:
#             print(f"Suggestions: {suggestions[:10]}")  # show first 10 suggestions
#         else:
#             print("No suggestions found.")


# if __name__ == "__main__":
#     main()



# main.py

# import sys
# sys.stdout.reconfigure(encoding="utf-8")

# import os
# from preprocessing import preprocess_dataset, preprocess_user_text
# from shingling import generate_shingles_for_books, generate_shingles
# from rolling_hash import hash_books_rolling, hash_user_text_rolling
# from plagiarism_checker import compare_with_books
# from scoring import compute_score, print_top_matches
# from trie_autocomplete import TrieNode, trie_insert, autocomplete

# # ----------------- Build Trie -----------------
# def build_trie_from_books(books):
#     print("\nBuilding trie for autocomplete...")
#     root = [None]  # pointer to root

#     for text in books.values():
#         words = text.split()
#         for word in words:
#             trie_insert(root, word)

#     print("✅ Trie built successfully from preprocessed books")
#     return root

# # ----------------- User Input with Autocomplete -----------------
# def get_user_input(trie_root):
#     print("\nType your text (autocomplete suggestions shown after each word, type 'submit' to finish):")
#     user_words = []

#     while True:
#         prefix = input("> ").strip()
#         if prefix.lower() == "submit":
#             break
#         user_words.append(prefix)

#         # show autocomplete suggestions
#         suggestions = autocomplete(trie_root, prefix)
#         if suggestions:
#             print("Suggestions:", ", ".join(suggestions[:5]))  # show top 5 suggestions

#     return " ".join(user_words)

# # ----------------- Main -----------------
# def main():
#     dataset_dir = "dataset/"

#     # 1️⃣ Preprocess all books
#     books = preprocess_dataset(dataset_dir)

#     for name, text in books.items():
#         print(f"{name}: {len(text.split())} words")

#     preprocessed_dir = os.path.join(dataset_dir, "preprocessed")
#     print(f"Preprocessed books saved in '{preprocessed_dir}'")

#     # 2️⃣ Generate shingles for books
#     shingles_dict = generate_shingles_for_books(books, k=5)

#     # 3️⃣ Save shingles
#     shingles_dir = os.path.join(dataset_dir, "shingles")
#     os.makedirs(shingles_dir, exist_ok=True)
#     for name, shingles in shingles_dict.items():
#         output_path = os.path.join(shingles_dir, name.replace(".txt", "_shingles.txt"))
#         with open(output_path, "w", encoding="utf-8") as f:
#             for shingle in shingles:
#                 f.write(shingle + "\n")
#         print(f"Shingles saved for {name} -> {output_path}")

#     # 4️⃣ Compute rolling hashes for all books
#     print("\nComputing rolling hashes for all books...")
#     hashes_dir = os.path.join(dataset_dir, "hashs")
#     os.makedirs(hashes_dir, exist_ok=True)
#     hash_books_rolling(books, k=5, output_dir=hashes_dir)
#     print(f"All rolling hashes saved in '{hashes_dir}'")

#     # 5️⃣ Build Trie for autocomplete
#     trie_root = build_trie_from_books(books)

#     # 6️⃣ Get user input with autocomplete
#     user_text = get_user_input(trie_root)

#     # 7️⃣ Preprocess user input
#     user_text_clean = preprocess_user_text(user_text)

#     # 8️⃣ Generate shingles & rolling hashes for user text
#     user_shingles = generate_shingles(user_text_clean, k=5)
#     user_hashes = hash_user_text_rolling(user_text_clean, k=5)

#     # 9️⃣ Compare user hashes with book hashes
#     results = compare_with_books(user_hashes, books_hashes_dir=hashes_dir)

#     # 🔟 Compute plagiarism scores & print top matches
#     scores = compute_score(results)
#     print_top_matches(scores, top_n=5)


# if __name__ == "__main__":
#     main()


import sys
sys.stdout.reconfigure(encoding="utf-8")

import os
from preprocessing import preprocess_dataset, preprocess_user_text
from shingling import generate_shingles_for_books, generate_shingles
from rolling_hash import hash_books_rolling, hash_user_text_rolling
from plagiarism_checker import compare_with_books
from scoring import compute_score, print_top_matches
from trie_autocomplete import TrieNode, trie_insert, autocomplete

# ----------------- Build Trie -----------------
def build_trie_from_books(books):
    print("\nBuilding trie for autocomplete...")
    root = [None]  # pointer to root

    for text in books.values():
        words = text.split()
        for word in words:
            trie_insert(root, word)

    print("✅ Trie built successfully from preprocessed books")
    return root

# ----------------- User Input with Autocomplete -----------------
def get_user_input(trie_root):
    print("\nType your text (autocomplete suggestions shown for last word, type 'submit' to finish):")
    user_words = []

    while True:
        # show current line
        current_line = " ".join(user_words)
        prefix = input(f"{current_line} > ").strip()

        if prefix.lower() == "submit":
            break

        # Split last word for autocomplete
        last_word = prefix.split()[-1] if prefix.split() else ""
        if last_word:
            suggestions = autocomplete(trie_root, last_word)
            if suggestions:
                print("Suggestions:", ", ".join(suggestions[:5]))  # top 5 suggestions

        # Add the full input to user_words
        user_words.extend(prefix.split())

    return " ".join(user_words)

# ----------------- Main -----------------
def main():
    dataset_dir = "dataset/"

    # 1️⃣ Preprocess all books
    books = preprocess_dataset(dataset_dir)
    for name, text in books.items():
        print(f"{name}: {len(text.split())} words")

    preprocessed_dir = os.path.join(dataset_dir, "preprocessed")
    print(f"Preprocessed books saved in '{preprocessed_dir}'")

    # 2️⃣ Generate shingles for books
    shingles_dict = generate_shingles_for_books(books, k=5)

    # 3️⃣ Save shingles
    shingles_dir = os.path.join(dataset_dir, "shingles")
    os.makedirs(shingles_dir, exist_ok=True)
    for name, shingles in shingles_dict.items():
        output_path = os.path.join(shingles_dir, name.replace(".txt", "_shingles.txt"))
        with open(output_path, "w", encoding="utf-8") as f:
            for shingle in shingles:
                f.write(shingle + "\n")
        print(f"Shingles saved for {name} -> {output_path}")

    # 4️⃣ Compute rolling hashes for all books
    print("\nComputing rolling hashes for all books...")
    hashes_dir = os.path.join(dataset_dir, "hashs")
    os.makedirs(hashes_dir, exist_ok=True)
    hash_books_rolling(books, k=5, output_dir=hashes_dir)
    print(f"All rolling hashes saved in '{hashes_dir}'")

    # 5️⃣ Build Trie for autocomplete
    trie_root = build_trie_from_books(books)

    from prompt_toolkit import PromptSession
    from prompt_toolkit.completion import Completer, Completion

    class TrieCompleter(Completer):
        def __init__(self, trie_root):
            self.trie_root = trie_root

        def get_completions(self, document, complete_event):
            word = document.get_word_before_cursor()
            suggestions = autocomplete(self.trie_root, word)
            for s in suggestions[:5]:  # top 5 suggestions
                yield Completion(s, start_position=-len(word))

    def get_user_input_live(trie_root):
        session = PromptSession()
        completer = TrieCompleter(trie_root)
        print("Type your text (live autocomplete, press Enter to submit):")
        user_input = session.prompt("> ", completer=completer)
        return user_input
    
    # 6️⃣ Get user input with live autocomplete
    user_text = get_user_input_live(trie_root)



    # 7️⃣ Preprocess user input
    user_text_clean = preprocess_user_text(user_text)

    # 8️⃣ Generate shingles & rolling hashes for user text
    user_shingles = generate_shingles(user_text_clean, k=5)
    user_hashes = hash_user_text_rolling(user_text_clean, k=5)

    # 9️⃣ Compare user hashes with book hashes
    results = compare_with_books(user_hashes, books_hashes_dir=hashes_dir)

    # 🔟 Compute plagiarism scores & print top matches
    scores = compute_score(results)
    print_top_matches(scores, top_n=5)

if __name__ == "__main__":
    main()
