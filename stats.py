import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

#function that takes the (text document path) and turns it into the "get_book_text" value
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

book = (get_book_text(book_path))

def word_list():
     #breaks all the text into a list of words
     words = book.split()
     return words

def get_num_words():
     #length of word list
     num_words = len(word_list())
     return num_words

def raw_letters():
    letter_count = {
         
    }
    for letter in book:
        low_letter = letter.lower() 
        if low_letter in letter_count:
            letter_count[low_letter] += 1
        else:
            letter_count[f"{low_letter}"] = 1
    return letter_count

def sort_on(raw_letters):
    return raw_letters["num"]

def letter_list(raw_letters):
    result = []

    for char, num in raw_letters.items():
        char_data = {"char": char, "num": num}
        result.append(char_data)

    result.sort(reverse=True, key=sort_on)
    return result

letters_dict = raw_letters()
sorted_letters = letter_list(letters_dict)

