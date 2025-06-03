def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

# User input
mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
text = input("Enter message: ")
shift = int(input("Enter shift value: "))

# Output result
print("Result:", caesar_cipher(text, shift, mode))
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

# User input
mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
text = input("Enter message: ")
shift = int(input("Enter shift value: "))

# Output result
print("Result:", caesar_cipher(text, shift, mode))
