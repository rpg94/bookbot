from stats import *

def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
    return book_contents

def main():
    # initialize variables
    book = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book)
    num_char_dict = get_num_chars(book)
    sorted_chars = sort_char_dict(num_char_dict)

    # format message
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(char["char"] + ": " + str(char["num"]))

main()