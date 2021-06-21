import string

letter_list = []
for i in string.ascii_lowercase:
    letter_list.append(i)


print(letter_list)
index = 0
while index < 6:
    print(letter_list[index], ord(letter_list[index]), letter_list[index + 10], ord(letter_list[index+10]), letter_list[index + 20], ord(letter_list[index+20]))
    index += 1
while index < 10:
    print(letter_list[index], ord(letter_list[index]), letter_list[index + 10], ord(letter_list[index+10]))
    index += 1

