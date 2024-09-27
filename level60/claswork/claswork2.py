from typing import Counter


def duplicate_count(text):
    counts = Counter(text.lower())
    return sum(1 for count in counts.values() if count > 1)
    