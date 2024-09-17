def separateString(s):
    numberString = ''.join(char for char in s if char.isdigit())  
    letterString = ''.join(char for char in s if char.isalpha())  
    return numberString, letterString

def convertToAscii(numberString, letterString):
    evenNumberAscii = [ord(num) for num in numberString if int(num) % 2 == 0]  
    uppercaseLetterAscii = [ord(char) for char in letterString if char.isupper()]  
    return evenNumberAscii, uppercaseLetterAscii

userInput = input("Enter a string: ")


numberString, letterString = separateString(userInput)
evenNumberAscii, uppercaseLetterAscii = convertToAscii(numberString, letterString)


print("Even Numbers ASCII Codes:", evenNumberAscii)
print("Uppercase Letters ASCII Codes:", uppercaseLetterAscii)
