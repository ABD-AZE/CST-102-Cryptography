# Simple Block Cipher Implementation

This project is a Python implementation of a basic block cipher with key permutation and cyclic shift operations to create simple encryption. The code takes an 8-bit plaintext and a 12-bit keyspace, permutes and encrypts the plaintext in two rounds, and produces an 8-bit ciphertext.

## Code Overview

The script performs the following steps:
1. **Permutation of Plaintext**: Rearranges the bits of the plaintext in a specific order.
2. **Round Key Generation**: Derives round keys by cyclically shifting parts of the keyspace.
3. **Encryption Rounds**: Performs two rounds of encryption, using XOR operations with the generated round keys.
4. **Final Permutation**: Re-arranges the bits of the result to produce the ciphertext.

## Functions

### 1. `PermutePlainText(PlainText)`
Rearranges the bits of the input plaintext based on a predefined order.

- **Input**: `PlainText` (string of 8 bits)
- **Output**: Permuted 8-bit string

### 2. `cylicalShift(In)`
Performs a left cyclic shift on a bit string.

- **Input**: `In` (string of bits)
- **Output**: Cyclically shifted bit string

### 3. `ithRoundKey(KeySpace, i)`
Generates the `i`-th round key by cyclically shifting specific parts of the keyspace.

- **Input**: 
  - `KeySpace` (12-bit string)
  - `i` (integer specifying the round)
- **Output**: 8-bit round key

### 4. `roundKeyFunction(Key, Text)`
XORs the key and text bit-by-bit to produce a new encrypted text.

- **Input**:
  - `Key` (8-bit string)
  - `Text` (8-bit string)
- **Output**: Encrypted 8-bit string after XOR

### 5. `finalPermutation(S)`
Applies a final permutation on the encrypted bit string to produce the ciphertext.

- **Input**: `S` (8-bit string)
- **Output**: Ciphertext (8-bit string)

### Example

```plaintext
Enter the 8 bit string of bits: 10101010
Enter the 12 bit keyspace: 110010101011
The Cipher text is:  00011001
