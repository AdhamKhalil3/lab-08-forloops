highestnum = 0


for i in range(0, 10):
    userinput = input("Lets party! How long until the party?")
    userInt = int(userinput)
    print("PARTY NOW! " + str(userinput))
    if userInt > highestnum - 1:
        highestnum = userInt
        print("PARTY TIME")
    


