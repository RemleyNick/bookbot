def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_counts = {}
    text = text.lower()  # convert entire text to lowercase

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_char_counts(char_counts):
    char_list = [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()]
    
    def get_num(entry):
        return entry["num"]
    
    char_list.sort(key=get_num, reverse=True)
    
    return char_list
