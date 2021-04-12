with open("enc","r") as fp:
    for c in fp.read().strip():
        c=ord(c)
        print(chr(c//256),end="")
        print(chr(c%256),end="")
print()
