with open("adat.txt") as adat:
    with open("adat2.txt", "w") as adat2:
        for line in adat:
            adat2.write(line)
