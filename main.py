import sys
from stats import count_words, count_characters 

def get_book_text(book):
    try:
        with open(book, encoding='utf-8-sig') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {book} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    text = get_book_text(book)
    if text is None: 
        print("Book not found or could not be read.")
        return
    
    num_words    = count_words(text)
    char_counts  = count_characters(text)   # ← Call the function here

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char, count in sorted(char_counts.items(), key=lambda item: item[1], reverse=True):
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
