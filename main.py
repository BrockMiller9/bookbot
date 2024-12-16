def main():
    path = "/home/brockmiller/workspace/github.com/Brockmiller9/bookbot/books/frankenstein.txt"
    text = read_book(path)
    # print(count_words(text))
    # print(count_letters(text))
    # print(text)
    print(print_main_report(text, path))

    
    

def read_book(path):
    with open(path) as f:
        return f.read()
        
def count_words(text):
    words = text.split()
    return len(words)
def count_letters(text):
    letter_count = {}

    for letter in text:
        if letter.lower() not in letter_count:
            letter_count[letter.lower()] = 1
        else:
            letter_count[letter.lower()] +=1
    return letter_count

def sort_on(dict):
    return dict["num"]

def print_main_report(book, path):
    word_count = count_words(book)
    letter_count = count_letters(book)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")

    print("")

    for letter in letter_count:
        if letter.isalpha():
            print(f"the '{letter}' character was found {letter_count[letter]}")

    print("--- End report ---")


main()

