def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #words = count_words(text)
    #print(f"Words in frankenstein-book: {words}")
    letters = num_letters(text)
    print(letters)


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

def num_letters(document):
    letters = {}
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for letter in alphabet:
        letters[letter] = 0
    lowered = document.lower()
    for letter in lowered:
        if letter in alphabet:
            letters[letter] += 1
    return letters


main()