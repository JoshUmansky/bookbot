import sys
from stats import get_word_count, get_char_count, sort_characters
def get_book_text(path):
    with open(path) as file:
        text = file.read()
    return text


def main():
    #file_path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    num_words = get_word_count(get_book_text(file_path))
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sort_characters(get_char_count(get_book_text(file_path)))
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    main()