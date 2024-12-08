def encryption(text, step): 
    result = ""
    for i in range(len(text)): 
        character = text[i] 

        if (character.isupper()):
            result += chr((ord(character) + step - 65) % 26 + 65)

        else:
            result += chr((ord(character) + step - 97) % 26 + 97)

    return result

stringtext = "caesar cipher"
step = 10
print("Text: " + stringtext)
print("Shift: " + str(step))
print("Cipher: " + encryption(stringtext, step))




