input_number = int(input("adj meg egy számot: "))
added_number = 0
while input_number < 10:
    added_number = added_number + input_number
    input_number = int(input("adj meg egy számot: "))

print(f"Az eddigi 10 alatti számok összege: {added_number}")
