
def get_book_text(filepath):
    with open(filepath) as text:
        file_contents = text.read()
    return file_contents

def which_book(filepath):
    book = get_book_text(filepath)
    return book

def count_words(filepath):
    words = which_book(filepath)
    count = len(words.split())
    return f"Found {count} total words"

def count_char(filepath):
    chars = {}
    book = which_book(filepath)
    book_lower = book.lower()
    for char in book_lower:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars
def sort_on(items):
    item_int = int(items["num"])
    return item_int
def char_dictionary(filepath):
    chars = count_char(filepath)
    char_dictionary = []
    i = 0
    for char in chars:
        char_dictionary.append({})
        char_dictionary[i] = {"name": f"{char}", "num": f"{chars[char]}"}
        i += 1
    char_dictionary.sort(reverse=True, key=sort_on)
    return char_dictionary

def report(filepath):
    word_count = count_words(filepath)
    chars_dictionary = char_dictionary(filepath)
    counter = 0
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for char in chars_dictionary:
        dic = chars_dictionary[counter]
        print(f"{dic["name"]}: {dic["num"]}")
        counter += 1
    print("============= END ===============")
