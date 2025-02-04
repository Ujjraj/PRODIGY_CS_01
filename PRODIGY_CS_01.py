def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Choose mode (encrypt/decrypt): ").lower()
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return
    
    result = caesar_cipher(message, shift, mode)
    
    print(f"The {mode}ed message is: {result}")

if __name__ == "__main__":
    main()