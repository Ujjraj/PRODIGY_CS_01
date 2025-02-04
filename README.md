# IMPLEMENTATION OF CEASAR CIPHER ALGORITHM

## DESCRIPTION

The Caesar Cipher is one of the earliest and most straightforward encryption methods, named after Julius Caesar, who famously used it to safeguard his confidential communications. This technique operates by shifting each letter in a message by a predetermined number of positions either forward or backward in the alphabet.


### How Does It Work?

#### *Encryption*
1. Choose a shift value (a number between 1 and 25). This is your password key.
2. For each letter in the message:
   - Shift the letter by the chosen number of positions in the alphabet.
   - If the shift goes past "Z" or "z", it wraps around to the beginning of the alphabet.
3. Non-alphabetic characters (like spaces, numbers, or punctuation) remain unchanged.

*Example*:
- *Message*: HELLO
- *Shift*: 3
- *Encrypted Message*: KHOOR  
  (H → K, E → H, L → O, L → O, O → R)

---

#### *Decryption*
1. Use the same shift value that was used for encryption.
2. For each letter in the encrypted message:
   - Shift the letter backward by the same number of positions in the alphabet.
   - If the shift goes before "A" or "a", it wraps around to the end of the alphabet.
3. Non-alphabetic characters remain unchanged.

*Example*:
- *Encrypted Message*: KHOOR
- *Shift*: 3
- *Decrypted Message*: HELLO  
  (K → H, H → E, O → L, O → L, R → O)
