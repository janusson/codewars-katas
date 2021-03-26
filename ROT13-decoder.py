# Hail Caesar.py
# ROT 13 decryption

"""
You are in the ancient Roman army and are Caesar's trusted companion and
military advisor. He confides in you about numerous plots he has thwarted to
take his life and tasks you to devise a way to keep secrets secret from his
enemies.

You begin by creating a shift cipher, where the values of the letters get
shifted by a specified (input) degree.

(exit story arc: A modern case of a shift cipher is the ROT13 cipher.
The values of the letters are shifted by 13 places;'A' to 'N', and 'B' ↔ to'O'.

Create a function which takes a ROT13 encoded string as input and outputs a
decoded string.

All letters are uppercase. Don't transform any non-alphabetic characters
like spaces or punctuation, but do pass them on to the output.

"""

# sample strings, encoded and decoded with ROT13
encoded = "GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK."
decoded = "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX."


def hailCaesar(enc_str):
    import string
    letters = list(string.ascii_uppercase)
    decode = []
    for letter in enc_str:
        if letter in letters:
            # find index, if letter in alphabet, undo ROT13, add to list
            decode.append(letters[letters.index(letter) - 13])
        else:
            # if non-alphabetic, add to list
            decode.append(letter)
    return ''.join(decode)  # reconstruct sentence


hailCaesar(encoded)
