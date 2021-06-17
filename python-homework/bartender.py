user_age = int(input("Add meg a korod: "))
user_drink = input("Add meg mit iszol: ")

if user_age < 18 and user_drink == "sör":
    print("Sajnos nem adhatok")
elif user_age > 60 and user_drink == "kóla":
    print("A koffein megemelheti a vérnyomását")
elif user_drink != "sör" and user_drink != "kóla":
    print("Csak sört és kólát tudunk adni")
elif user_drink == "sör":
    print("Parancsoljon, a söre")
else:
    print("Parancsoljon, a kólája")