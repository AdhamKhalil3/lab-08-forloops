for listednumb in range(1,101):
    if listednumb %3 == 0 and listednumb %5 == 0:
        print("fizzbuzz")
    elif listednumb %3 == 0:
        print("fizz")
    elif listednumb %5 == 0:
        print("buzz")
    else:
        print(str(listednumb))