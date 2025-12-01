from stats import word_count, char_count

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    total_words = word_count(book_text)
    total_characters = char_count(book_text)
    print(f"Found {total_words} total words")
    print(total_characters)

main()