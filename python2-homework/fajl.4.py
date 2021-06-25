with open("adat.txt", "r") as text:
    my_text = text.read().split()
joined_list = " ".join(my_text)
index = 0
with open("adat2.txt", "a") as f:
    for i in joined_list:
        f.write(joined_list[index])
        index += 1
