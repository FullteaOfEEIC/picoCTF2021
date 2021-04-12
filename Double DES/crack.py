from pwn import *
from tqdm.auto import tqdm
from Crypto.Cipher import DES
from multiprocessing import Pool
import string


def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()


def get_encrypted():
    io = remote("mercury.picoctf.net", 3620)
    io.recvline()
    encrypted = io.recvline().strip()
    return encrypted


def crack(d):
    encrypted = d[0]
    key1 = d[1]
    key1 = pad(str(key1))
    des1 = DES.new(key1, DES.MODE_ECB)
    dec_1step = des1.decrypt(encrypted)
    for key2 in range(10**6):
        key2 = pad(str(key2))
        des2 = DES.new(key2, DES.MODE_ECB)
        dec = des2.decrypt(dec_1step)
        try:
            dec = dec.decode()
            print(dec)
        except UnicodeDecodeError:
            pass

if __name__=="__main__":
    encrypted = get_encrypted()
    #encrypted=b'ed076cec2f79a5fd137938132f73ffffb7029745516d51c41dadb1eafed2c709076b57223076ed7f'
    encrypted = binascii.unhexlify(encrypted)
    print(encrypted)
    print()
    print()
    params =[(encrypted,i) for i in range(10**6)]
    with Pool() as p:
        imap =p.imap(crack, params)
        list(tqdm(imap, total=len(params)))
