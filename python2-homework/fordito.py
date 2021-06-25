my_list = []
my_input = int(input("Adj meg egy számot: "))
while my_input != 0:
    my_list.append(my_input)
    my_input = int(input("Adj meg egy számot: "))

print(my_list[::-1])

