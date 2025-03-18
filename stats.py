def get_num_words(file):
    count = 0
    num_dict ={}
    with open(file) as f:
        file_contents = f.read()
    words = file_contents.split()
    for word in words:
        count += 1
    return count

def num_dict(file):
    num_dict = {}
    with open(file) as f:
        file_contents = f.read()
    words = file_contents.split()
    for word in words:
        for letter in word.lower():
            if letter in num_dict:
                num_dict[letter] += 1
            else:
                num_dict[letter] = 1
    return num_dict

def sort_dict(char_dict):
    list_dict = []
    for char, count in char_dict.items():
        if char.isalpha(): 
            list_dict.append({"char": char, "count": count})

    list_dict.sort(key=lambda d: d["count"], reverse=True)

    return list_dict
