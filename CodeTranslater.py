import string

def EncodeCeasarCode(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

def DecodeCeasarCode(text, alphabets):

    arr = []
    for i in range(1,27):
        arr.append(EncodeCeasarCode(text, i, alphabets))
    return arr

def DecodeVigenege(code, key):

    codes = list(code)
    alphabetss = list(string.ascii_lowercase)
    keys = list(key)
    WhereIsCode = []
    for i in range(0, len(key)):
        for j in range(0, 26):
            if (alphabetss[j] == keys[i]):
                WhereIsCode.append(j)
                break
    EncodedVigenege = []
    for i in range(0, len(code)):
        EncodedVigenege.append(EncodeCeasarCode(codes[i], WhereIsCode[i],[string.ascii_uppercase, string.ascii_lowercase, string.punctuation]))

    return ''.join(EncodedVigenege)


