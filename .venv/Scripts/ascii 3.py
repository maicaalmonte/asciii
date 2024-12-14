import art

# Caesar cipher function
def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                result.append(chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a')))
            elif char.isupper():
                result.append(chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A')))
        else:
            result.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(result)

# Generate ASCII art text
ascii_art = art.text2art("Pretty")

# Apply Caesar cipher to the ASCII art
shift = 5  # You can adjust the shift value here
encrypted_art = caesar_cipher(ascii_art, shift)

# Display the original and encrypted ASCII art
print("Original ASCII Art:")
print(ascii_art)
print("Encrypted ASCII Art:")
print(encrypted_art)
