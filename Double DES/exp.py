from Crypto.Cipher import DES
import random
import string

def generate_key():
    return pad("".join(random.choice(string.digits) for _ in range(6)))
def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

key = generate_key()
print(key)

message="picoCTF{oh... this is dummy}"
message = pad(message)

des = DES.new(key, DES.MODE_ECB)
enc_msg = des.encrypt(message)
print(enc_msg)
des2 = DES.new(key, DES.MODE_ECB)
dec_msg = des2.decrypt(enc_msg)
print(dec_msg)
