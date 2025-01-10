def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 
    words_list = count_words(file_contents)
    word_count = len(words_list)
    letter_count = count_char(file_contents)
    
def count_words(string):
    words = string.split()
    return words

def count_char(string):
    char_dict = create_letter_dict()
    string = string.lower()
    for letter in string:
        if 96 < ord(letter) < 123:
            char_dict[letter] += 1
    return char_dict

def create_letter_dict():
    char_dict = {}
    for i in range(97, 123):
        char_dict[chr(i)] = 0
    return char_dict

main()