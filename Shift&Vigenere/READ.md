# README.md

## Shift Cipher and Vigenere Cipher Implementations

This directory contains two Python scripts that implement the Shift Cipher and Vigenere Cipher encryption and decryption methods.

### Shift Cipher

The Shift Cipher script includes the following functions:

- `sanitize_input(text)`: Removes special characters and whitespaces, and converts the text to lowercase.
- `shift_cipher(text, key)`: Encrypts the sanitized text using the shift cipher.
- `shift_decipher(text, key)`: Decrypts the cipher text using the shift cipher.
- `frequency_analysis(ciphertext)`: Decodes the ciphertext using frequency analysis.

### Vigenere Cipher

The Vigenere Cipher script includes the following functions:

- `generate_key(msg, key)`: Generates a key that matches the length of the message.
- `encrypt_vigenere(msg, key)`: Encrypts the message using the Vigenere cipher.
- `decrypt_vigenere(msg, key)`: Decrypts the message using the Vigenere cipher.
