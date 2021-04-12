import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

encrypted = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"


def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


def b16_decode(enc):
    plain = ""
    for i in range(0, len(enc), 2):
        c1, c2 = enc[i], enc[i + 1]
        ind1 = ALPHABET.find(c1)
        ind2 = ALPHABET.find(c2)
        plain += chr(ind1*16+ind2)
    assert b16_encode(plain) == enc
    return plain


for key in ALPHABET:
    dec = ""
    for i, c in enumerate(encrypted):
        dec += shift(c, key[i % len(key)])
    flag = b16_decode(dec)
    print(flag)
