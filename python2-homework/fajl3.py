with open("adat.txt", "r") as text:
    my_text = text.read()
my_list = list(my_text.split())
joined_list = " ".join(my_list)
with open("adat2.txt", "a") as f:
    f.write(joined_list)
