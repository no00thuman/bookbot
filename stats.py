def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words


def count_characters(text):
    text = text.lower()
    total = {}
    for ch in text:
        if ch in total:
            total[ch] += 1
        else:
            total[ch] = 1
    return total


def sort_characters(char_counts):
    char_list = []
    for char, num in char_counts.items():   # ✅ fixed .items
        char_list.append({"char": char, "num": num})
    # ✅ sort list of dicts by "num" (largest first)
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list



