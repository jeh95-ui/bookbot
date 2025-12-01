def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowercased_text = text.lower()
    char_frequency = {}
    for char in lowercased_text:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency