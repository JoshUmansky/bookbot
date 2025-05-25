def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lower_text = text.lower()
    char_count = []
    for char in lower_text:
        found = False
        for dict in char_count:
            if dict["char"] == char:
                dict["num"] += 1
                found = True
        if not found:
            char_count.append({"char": char, "num": 1})
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_characters(char_count):
    char_count.sort(reverse=True, key=sort_on)
    for dict in char_count:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    return 0
    
