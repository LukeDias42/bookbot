def get_book(file_path):
    with open("./books/frankenstein.txt") as book:
        return book.read()


def count_words(book):
    return len(book.split(" "))


def count_characters(book):
    char_counter = {}
    for char in book.lower():
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    return char_counter


def sorter(dic):
    return dic["value"]


def get_sorted_count_character_list(character_counter):
    sorted_list = []
    for char in character_counter:
        sorted_list.append({"char": char, "value": character_counter[char]})
    sorted_list.sort(reverse=True, key=sorter)
    return sorted_list


def main():
    book = get_book("./books/frankenstein.txt")
    print(count_words(book))
    char_dic = count_characters(book)
    sorted_list = get_sorted_count_character_list(char_dic)
    for element in sorted_list:
        if element["char"].isalpha():
            print(f"The character {element["char"]} appears {element["value"]} times")


main()

