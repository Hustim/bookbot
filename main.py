def main():
    book_route = "books/frankenstein.txt"
    with open(book_route) as f:
        file_contents = f.read() #string
    words_list = split_string(file_contents) #list
    word_count = len(words_list) #int
    letter_count = sort_by_count(count_char(file_contents)) #list of dictionaries
    print_report(word_count, letter_count, book_route)
    
def split_string(string): #splits string, returns list of words
    words = string.split()
    return words

def count_char(string): #lower-casses all letters, returns dictionary {letter: count}
    char_dict = create_letter_dict()
    string = string.lower()
    for letter in string: #counts letters based on their ASCII value
        if 96 < ord(letter) < 123:
            char_dict[letter] += 1
    return char_dict

def create_letter_dict(): #creates dictionary of lower case letters in alphabetical order, values set to 0
    letter_dict = {}
    for i in range(97, 123):
        letter_dict[chr(i)] = 0
    return letter_dict

def sort_on(dict):
    return dict["num"]

def sort_by_count(letter_dict): #sorts dictionary of letters by count (from highest), returns list of dictionaries
    letter_dict_list = []
    for letter in letter_dict: #converts dictionary to list of dictionaries for sorting purposes
        letter_dict_list.append({"name": letter, "num": letter_dict[letter]})
    letter_dict_list.sort(reverse=True, key=sort_on)
    return letter_dict_list

def print_report(word_count, letter_count, route): #prints formatted report onto console
    print(f"--- Begin report of {route} ---") 
    print(f"{word_count} words found in document\n")
    for dict in letter_count:
        print(f"The \'{dict["name"]}\' character was found {dict["num"]} times")
    print("--- End report ---")
main()