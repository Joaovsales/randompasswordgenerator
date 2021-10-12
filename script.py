from random import randint
possibleCharacters = [33, 35, 42, 43, 48, 49, 50, 51, 52, 53, 54, 55, 56, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 127]

def createRandomPassword(qt):
    password = ""
    for i in range(qt):
        if i == 0:
            digit = chr(randint(0, len(possibleCharacters)))
            while digit == "." or digit == "-":
                digit = chr(randint(0, len(possibleCharacters)))
            password += digit
        else:
            digit = chr(randint(0, len(possibleCharacters)))
            password += digit
    return password


#Option of how many characters
charactersQt = int(input("How many characters in your password? "))
password = createRandomPassword(charactersQt)
print("Your password is: ", password)
