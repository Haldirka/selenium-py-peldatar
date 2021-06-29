my_list = []
my_input = int(input("Adj meg egy számot: "))
while my_input != 0:
    if my_input > 0:
        my_list.append(my_input)
        my_input = int(input("Adj meg egy számot: "))
    else:
        my_input = int(input("Adjon meg pozitív számot: "))

print(my_list[::-1])

