# Feistel Cryptosystem

This project implements a simple Feistel cryptosystem with 3 rounds of encryption. The Feistel structure is a symmetric structure used in the construction of block ciphers, which divides the plaintext into two halves and processes them through multiple rounds of substitution and permutation.

## Functions

### `singleRound(LR, generatedKey)`

This function performs a single round of the Feistel encryption process.

- **Parameters:**
    - `LR` (str): The input string, which is a combination of the left and right halves of the plaintext.
    - `generatedKey` (str): The key used for the current round of encryption.

- **Returns:**
    - `L1` (str): The result after one round of the Feistel encryption.

### `FiestelSystem3RoundsEncrypt(Ptext, Key)`

This function performs the Feistel encryption process over 3 rounds.

- **Parameters:**
    - `Ptext` (str): The 8-bit plaintext to be encrypted.
    - `Key` (str): The 12-bit key used for generating round keys.

- **Returns:**
    - `final` (str): The 8-bit ciphertext after 3 rounds of Feistel encryption.

## Usage

1. The user is prompted to enter an 8-bit plaintext.
2. The user is prompted to enter a 12-bit key.
3. The `FiestelSystem3RoundsEncrypt` function is called with the provided plaintext and key.
4. The resulting ciphertext is printed.

## Example
