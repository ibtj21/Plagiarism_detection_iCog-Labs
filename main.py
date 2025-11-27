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
    hash_books_rolling(shingles_dict, output_dir=hashes_dir)
    print(f"All rolling hashes saved in '{hashes_dir}'")

    # 5️⃣ Build Trie for autocomplete
    trie_root = build_trie_from_books(books)

    from prompt_toolkit import PromptSession
    from prompt_toolkit.completion import Completer, Completion # Makes it real-time autocomplete, instead of showing suggestions only after pressing Enter

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
