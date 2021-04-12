from hashlib import sha1

#prepare 2 pdfs (shattered-1.pdf and shattered-2.pdf), which are different and have the same hash.
#I prepared pdfs from https://shattered.io/
collision1 = open("shattered-1.pdf","rb").read()
collision2 = open("shattered-2.pdf","rb").read()
invite = open("invite.pdf","rb").read()
assert sha1(collision1).hexdigest() == sha1(collision2).hexdigest()

assert sha1(collision1+invite[-1000:]).hexdigest() == sha1(collision2+invite[-1000:]).hexdigest()
ans1 = open("anser1.pdf","wb")
ans1.write(collision1+invite[-1000:])
ans2 = open("anser2.pdf","wb")
ans2.write(collision2+invite[-1000:])
