def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    print(f"Words in frankenstein-book: {words}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    #amount = 0
    #for words in words:
    #    amount += 1
    #return amount
    return len(words)

main()