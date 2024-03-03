def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def main():
    text = input("Enter text to encrypt/decrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted/Decrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
