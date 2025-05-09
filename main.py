import sys
from stats import book_path
from stats import raw_letters
from stats import sorted_letters
from stats import get_num_words

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words()} total words")
    print("--------- Character Count -------")
    
    for item in sorted_letters:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['num']}")
    
    print("============= END ===============")
            

main()