import sys

def encrypt(text, shift):
    result = ''
    text = text.upper()
    count = 0

    for char in text:
        if 'A' <= char <= 'Z':
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += shifted
            count += 1
            if count % 5 == 0:
                result += ' '
            if count % 50 == 0:
                result += '\n'

    return result.strip()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 mycipher.py <shift>")

    shift = int(sys.argv[1])

    plaintext = ''
    for line in sys.stdin:
        plaintext += line

    ciphertext = encrypt(plaintext, shift)
    print(ciphertext)

