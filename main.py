def main():
    book_path = "books/frankenstein.txt"
    #text = get_book_text(book_path)
    #words = count_words(text)
    #print(f"Words in frankenstein-book: {words}")
    #letters = num_letters(text)
    #print(letters)
    doc_report(book_path)


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

# My count letters
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

# Boot.Dev count letters
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def doc_report(document_path):
    print(f"--- Begin report of {document_path} ---")
    text = get_book_text(document_path)
    words = count_words(text)
    print(f"{words} words found in the document\n")
    characters = get_chars_dict(text)#num_letters(text)
    letters = []
    nums = []
    d = {}
    for char in characters:
        if char.isalpha():
            letters.append({"char": char, "num": characters[char]})
            #num = characters[char]
            #nums.append(num)
        #print(f"The letter '{letter}' character was found {times} times")
    letters.sort(reverse= True, key=sort_on)
    #for i in range(len(letters)):
    #    print(f"The letter '{letters[i]}' character was found {nums[i]} times")
    for alph in letters:
        print(f"The '{alph['char']}' character was found {alph['num']} times")
    print("--- End report ---")

main()