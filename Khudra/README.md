# Khudra Encryption Algorithm

This project implements the encryption algorithm for **Khudra**, a lightweight block cipher designed for constrained environments. The encryption process involves 18 rounds, each incorporating a custom S-box substitution, permutation, and round key mixing.

## How It Works

Khudra uses a key size of 80 bits and a block size of 64 bits, suitable for lightweight cryptography applications. Each round transforms the block using the following steps:

1. **S-box Substitution**: A substitution operation based on a predefined S-box, which replaces parts of the plaintext to add non-linearity.
2. **Permutation**: A permutation function is applied in multiple rounds to change the order of bits, further obfuscating the data.
3. **Round Key Mixing**: In each round, the plaintext undergoes an XOR operation with a round-specific key derived from the main key using a key scheduling function.

## Functions

- `s(t)`: Substitution function using a predefined S-box.
- `F_func_singleround(P)`: Single-round permutation function that rearranges the 64-bit plaintext using the S-box.
- `F(P)`: Applies six rounds of `F_func_singleround(P)` for additional diffusion.
- `keyschedule(K, i)`: Derives the round key for the `i`th round using the main 80-bit key.
- `encryptSingleRound(K, P, i)`: Executes a single round of encryption, incorporating S-box substitution, permutation, and key mixing.
- `encrypt(K, P)`: Main function to encrypt the plaintext by executing 18 rounds using `encryptSingleRound`.

## Usage

The script takes a 64-bit plaintext and an 80-bit key, both provided in hexadecimal format, and outputs the 64-bit ciphertext.
