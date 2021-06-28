import csv

with open("table_in.csv", "r", encoding="utf-8") as file1:
    with open("table_in_copy.csv", "w", encoding="utf-8") as file2:
        file1_read = csv.reader(file1, delimiter=",")
        for i in file1_read:
            file2.write(str(i[0]))
            file2.write(", ")
            file2.write(str(i[1]))
            file2.write("\n")