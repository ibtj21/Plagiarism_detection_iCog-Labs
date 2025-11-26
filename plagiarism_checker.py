def compare_with_books(user_hashes, books_hashes_dir="dataset/hashs/"):
    import os
    results = {}

    for filename in os.listdir(books_hashes_dir):
        if filename.endswith("_hashes.txt"):
            file_path = os.path.join(books_hashes_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                book_hashes = [int(line.strip()) for line in f]

            matches = sum(1 for h in user_hashes if h in book_hashes)

            # Longest consecutive match
            longest_consec = 0
            current = 0
            book_set = set(book_hashes)
            for h in user_hashes:
                if h in book_set:
                    current += 1
                    longest_consec = max(longest_consec, current)
                else:
                    current = 0

            results[filename.replace("_hashes.txt", "")] = {
                "matches": matches,
                "longest_consecutive": longest_consec,
                "total_user_shingles": len(user_hashes)
            }

    return results
