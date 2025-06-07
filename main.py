from stats import get_num_words, get_num_chars

def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
    return book_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book)
    print(f"{num_words} words found in the document")
    print(get_num_chars(book))

main()