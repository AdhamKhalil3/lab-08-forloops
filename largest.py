highestnum = 0
# initate highstnum variable as 0
# we will replace this 0 inside our loop

for i in range(0, 4, 1):
    userinput = input("Number please..")
    userInt = int(userinput)
    print("user entered: " + str(userinput))
    if userInt > highestnum:
        highestnum = userInt
        print("Updating highest number...")
    else:
        print("this is not the highest number")
print("the highest number entered is: " + str(highestnum))