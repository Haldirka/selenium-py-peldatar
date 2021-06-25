with open("adat.txt", "r") as text:
    my_text = text.read()
my_list = list(my_text.split())
for i in range(len(my_list)):
    print(my_list[i], end=" ")