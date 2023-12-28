from collections import Counter


def count_letters(sentence):
    sentence = sentence.lower().replace(" ", "")
    letter_counts = Counter(sentence)
    sorted_counts = sorted(letter_counts.items(),
                           key=lambda x: x[1], reverse=True)
    for letter, count in sorted_counts:
        print(f"{letter}: {count}")


# Example usage:
count_letters("hello world")
