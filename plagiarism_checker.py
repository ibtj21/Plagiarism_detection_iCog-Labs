def compare_with_books(user_hashes, books_hashes_dir="dataset/hashs/"):
    import os
    results = {}

    def longest_true_consecutive(user_hashes, book_hashes):
        # Map hash → its positions in the book
        positions = {}
        for i, h in enumerate(book_hashes):
            if h not in positions:
                positions[h] = []
            positions[h].append(i)

        longest = 0

        # Try aligning each user shingle to book positions
        for i in range(len(user_hashes)):
            current_hash = user_hashes[i]

            if current_hash not in positions:
                continue

            for pos in positions[current_hash]:
                length = 1
                j = i + 1
                k = pos + 1

                while j < len(user_hashes) and k < len(book_hashes):
                    if user_hashes[j] == book_hashes[k]:
                        length += 1
                        j += 1
                        k += 1
                    else:
                        break

                longest = max(longest, length)

        return longest

    for filename in os.listdir(books_hashes_dir):
        if filename.endswith("_hashes.txt"):
            file_path = os.path.join(books_hashes_dir, filename)

            with open(file_path, "r", encoding="utf-8") as f:
                book_hashes = [int(line.strip()) for line in f]

            book_set = set(book_hashes)

            # Total matches (scattered)
            matches = sum(1 for h in user_hashes if h in book_set)

            # ✅ consecutive plagiarism detection
            longest_consec = longest_true_consecutive(user_hashes, book_hashes)

            results[filename.replace("_hashes.txt", "")] = {
                "matches": matches,
                "longest_consecutive": longest_consec,
                "total_user_shingles": len(user_hashes)
            }

    return results
