from pwn import *
import string
from tqdm import tqdm
from collections import Counter
from functools import lru_cache

io = remote("mercury.picoctf.net", 50075)
flag = io.recvline().strip().decode()
flag = flag[6:]
n = io.recvline().strip().decode()
n = n[3:]
e = io.recvline().strip().decode()
e = e[3:]


def encrypt(s):
    io.sendline(s)
    enc = io.recvline().strip().decode()
    enc = enc[50:]
    return enc


@lru_cache()
def get(c, i):
    enc = encrypt("a" * (i - 1) + c)
    for j in range(1, i):
        enc = enc.replace(get("a", j), "")
    return enc


dec = ""
for i in range(1, 30):
    for j in range(33, 127):
        c = chr(j)
        enc = get(c, i)
        if enc in flag:
            print(c, end="")
            break
print()
