def szokoev (i):
    if i % 400 == 0:
        return True
    elif i % 100 == 0:
        return False
    elif i % 4 == 0:
        return True
    else:
        return False

input_ev = int(input("Adj meg egy évet: "))
if szokoev(input_ev) == True:
    print("Szökőév")
else:
    print("Nem szökőév")