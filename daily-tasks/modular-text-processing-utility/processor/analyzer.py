def word_count(text):
    words = text.split()
    return len(words)


def char_count(text):
    count = 0
    for ch in text:
        if ch != " ":
            count = count + 1
    return count