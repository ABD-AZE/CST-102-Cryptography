import string

def sanitize_input(text):
    """Remove special characters and whitespaces, and convert to lowercase."""
    allowed_chars = string.ascii_lowercase
    sanitized = ''.join([char.lower() for char in text if char.lower() in allowed_chars])
    return sanitized


def shift_cipher(text, key):
    """Encrypt the sanitized text using the shift cipher."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_index = (ord(char) - ord('a') + key) % 26
            encrypted_text += chr(shifted_index + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text


def shift_decipher(text, key):
    """Decrypt the cipher text using the shift cipher."""
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_index = (ord(char) - ord('a') - key) % 26
            decrypted_text += chr(shifted_index + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

def frequency_analysis(ciphertext):
    """Decode the ciphertext using frequency analysis."""
    english_freq = "etaoinshrdlcumwfgypbvkjxqz"
    
    letter_count = {char: 0 for char in string.ascii_lowercase}
    for char in ciphertext:
        if char.isalpha():
            letter_count[char] += 1
    
    sorted_letters = sorted(letter_count, key=letter_count.get, reverse=True)
    
    possible_shifts = []
    for i in range(len(english_freq)):
        shift = (ord(sorted_letters[0]) - ord(english_freq[i])) % 26
        possible_shifts.append(shift)
    
    decoded_strings = [shift_decipher(ciphertext, shift) for shift in possible_shifts]
    
    return decoded_strings[0]

def main():
    input_string = input("Enter the string to be encrypted: ")
    key = int(input("Enter the key (integer): "))
    
    sanitized_string = sanitize_input(input_string)
    encrypted_string = shift_cipher(sanitized_string, key)
    print(f"Encrypted String: {encrypted_string}")
    
    decrypted_string = shift_decipher(encrypted_string, key)
    print(f"Decrypted String: {decrypted_string}")
    
    freq_analysis_decoded = frequency_analysis(encrypted_string)
    print(f"Frequency Analysis Decoded String: {freq_analysis_decoded}")


main()
