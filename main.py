def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words_list = count_words(file_contents)
    word_count = len(words_list)
    print(word_count)
    
def count_words(string):
    words = string.split()
    return words




main()