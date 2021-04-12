from pwn import *
KEY_LEN = 50000
from tqdm.auto import tqdm
import binascii
import string

#encrypted= "551257106e1a52095f654f510a6b4954026c1e0304394100043a1c5654505b6b"
encrypted = "551257106e1a52095f654f510b6b4954026c1e0304394100043a1c5654505b6b"


def get_message(slide, encrypted):

    io = remote("mercury.picoctf.net", 36449)
    for i in range(4):
        io.recvline()
    io.sendline("1"*(50000-slide))
    io.recvline()
    io.recvline()

    print("load end")

    io.sendline(deconvert(encrypted))
    io.recvline()
    io.recvline()
    message = io.recvline().strip()
    #print(binascii.a2b_hex(message))
    return message


def convert(message):
    key = (chr(0)*len(message)).encode()
    result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), message, key))
    return "".join(result)

def deconvert(message):
    dec = b""
    for i in range(0,len(message),2):
        dec+=chr(int(message[i:i+2],16)).encode()
    return dec

print(deconvert(encrypted))

message = get_message(32, encrypted)
print(message)
message_dec = deconvert(message)
print(message_dec)
