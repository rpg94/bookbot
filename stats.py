def get_num_words(book_contents):
    num_words = len(book_contents.split())
    return num_words

def get_num_chars(book_contents):
    num_chars = {}
    chars = list(book_contents.lower())
    for char in chars:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def sort_char_dict(char_dict):
    dict_list = []
    for dict in sorted(char_dict.items(), key=lambda x: x[1], reverse=True):
        dict_list.append({"char": dict[0], "num": dict[1]})
    return dict_list