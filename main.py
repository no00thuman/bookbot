import sys
from stats import get_book_text,get_num_words,count_characters,sort_characters

def main():
        # check if a book path was provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)   # exit with error code 1

    path_to_book = sys.argv[1]   # second argument is the file path


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")

    text = get_book_text(path_to_book)

    # Word count
    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    # Character count
    print("--------- Character Count -------")
    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)

    for item in sorted_chars:
        ch = item["char"]
        n = item["num"]
        if ch.isalpha():           # only letters (includes accented letters)
            print(f"{ch}: {n}")

    print("============= END ===============")

if __name__ == "__main__":
    main()

    

