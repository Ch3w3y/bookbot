def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_count_dic = {}
    for char in text:
        char = char.lower()
        if char in char_count_dic:
            char_count_dic[char] += 1
        else:
            char_count_dic[char] = 1
    return(char_count_dic)

def sorted_dictionary(dictionary):
    result_list = []
    for char, count in dictionary.items():
        char_data = {"char": char, "count": count}
        result_list.append(char_data)

    result_list.sort(reverse=True, key=lambda dict_item: dict_item["count"])
    return result_list