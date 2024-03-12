with open("books/frankenstein.txt") as f:
    contents = f.read()
    print(contents)

txt_string = contents
words =txt_string.split()
number_word = len(words)
print(number_word)

my_string = txt_string
lowered_string = my_string.lower()
char_counts = {}
for i in lowered_string:    
    if i.isalpha():

        if i in char_counts:
            char_counts[i] += 1
    else:
        char_counts[i] = 1

    if i in char_counts:
        char_counts[i] += 1
    else:
        char_counts[i] = 1
print(char_counts)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

