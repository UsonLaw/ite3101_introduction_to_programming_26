def censor(text, word):
    words = text.split()
    stars = "*" * len(word)
    for i in range(len(words)):
        if words[i] == word:
            words[i] = stars
    return " ".join(words)
