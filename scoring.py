# scoring.py

def compute_score(results):
    """
    Compute plagiarism score (%) for each book, including a boost for longest consecutive match.
    Normalized to 0-100%.

    Parameters:
    - results: dict returned by compare_with_books(), format:
        {
            'BookName': {
                'matches': int,
                'longest_consecutive': int,
                'total_user_shingles': int
            },
            ...
        }

    Returns:
    - scores: dict {BookName: plagiarism_percentage}
    """
    scores = {}

    for book, data in results.items():
        total = data["total_user_shingles"]
        matches = data["matches"]
        longest = data["longest_consecutive"]

        if total == 0:
            score = 0
        else:
            # Base score: fraction of matching shingles
            base = matches / total

            # Boost factor: fraction of longest consecutive match
            boost = longest / total

            # Final weighted plagiarism score, capped at 100%
            score = base * (1 + boost) * 100
            score = min(score, 100)

        scores[book] = round(score, 2)

    return scores


def print_top_matches(scores, top_n=5):
    """
    Print top N books with highest plagiarism score.
    """
    sorted_books = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    print(f"\nTop {top_n} potential matches:")
    for book, score in sorted_books[:top_n]:
        print(f"{book}: {score}%")
