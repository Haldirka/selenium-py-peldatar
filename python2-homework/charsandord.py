my_dict = dict()
with open("text.txt", "r") as text:
    my_text_list = text.read().lower().split()
index = 0
amount_of_words = 1
for i in my_text_list:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1
for i, k in my_dict.items():
    print(f"{i} előfordulások száma: {k}")
