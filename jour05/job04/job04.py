def caesar_cipher(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

message = input("Entrez le message à chiffrer : ")
shift = int(input("Entrez le décalage à utiliser : "))

ciphered_message = caesar_cipher(message, shift)

print("Message chiffré : ", ciphered_message)