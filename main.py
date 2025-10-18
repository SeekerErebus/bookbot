import sys
import stats

def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    target_book = sys.argv[1]

    text = get_book_text(target_book)
    output_text = f"""============ BOOKBOT ============
Analyzing book found at {target_book}...
----------- Word Count ----------
Found {stats.get_num_words(text)} total words
--------- Character Count -------
"""
    char_dict = stats.get_sorted_char_dict(text)
    for item in char_dict:
        if not item['char'].isalpha():
            continue
        output_text += f"""{item['char']}: {item['num']}
"""
    output_text += "============= END ==============="
    print(output_text)

frankenstein = "books/frankenstein.txt"

main()