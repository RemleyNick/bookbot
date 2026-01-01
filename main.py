import sys
from stats import get_num_words, count_characters, sort_char_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    
    # Word count
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    # Character counts
    char_counts = count_characters(book_text)
    
    # Sort characters descending by count, alpha chars only
    sorted_chars = sort_char_counts(char_counts)
    
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    
    print("============= END ===============")



main()
