# # main.py

# from preprocessing import preprocess_dataset
# import os

# def main():
#     dataset_dir = "dataset/"

#     # Preprocess all books
#     books = preprocess_dataset(dataset_dir)

#     # Print word counts
#     for name, text in books.items():
#         print(f"{name}: {len(text.split())} words")

#     # Print where the preprocessed books are saved
#     preprocessed_dir = os.path.join(dataset_dir, "preprocessed")
#     print(f"Preprocessed books saved in '{preprocessed_dir}'")


# if __name__ == "__main__":
#     main()


# main.py

from preprocessing import preprocess_dataset
from shingling import generate_shingles_for_books
import os
import pickle  # optional, for saving shingles efficiently

def main():
    dataset_dir = "dataset/"

    # 1️⃣ Preprocess all books
    books = preprocess_dataset(dataset_dir)

    # Print word counts
    for name, text in books.items():
        print(f"{name}: {len(text.split())} words")

    # Print where the preprocessed books are saved
    preprocessed_dir = os.path.join(dataset_dir, "preprocessed")
    print(f"Preprocessed books saved in '{preprocessed_dir}'")

    # 2️⃣ Generate shingles for all preprocessed books
    shingles_dict = generate_shingles_for_books(books, k=5)  # k=5 words per shingle

    # 3️⃣ Save shingles into a new subfolder: dataset/shingles/
    shingles_dir = os.path.join(dataset_dir, "shingles")
    os.makedirs(shingles_dir, exist_ok=True)

    for name, shingles in shingles_dict.items():
        # save as a text file or pickle
        output_path = os.path.join(shingles_dir, name.replace(".txt", "_shingles.txt"))
        with open(output_path, "w", encoding="utf-8") as f:
            for shingle in shingles:
                f.write(shingle + "\n")
        print(f"Saved shingles for {name} -> {output_path}")

    print(f"All shingles saved in '{shingles_dir}'")


if __name__ == "__main__":
    main()
