import binascii

c=8533139361076999596208540806559574687666062896040360148742851107661304651861689
n=769457290801263793712740792519696786147248001937382943813345728685422050738403253
e=65537
p=1617549722683965197900599011412144490161
q=475693130177488446807040098678772442581573
assert p*q==n

def lcm(p,q):
    return (p*q)//gcd(p,q)
def gcd(p,q):
    if min(p,q)==0:
        return max(p,q)
    return gcd(min(p,q),max(p,q)%min(p,q))

d = pow(e,-1,lcm(p-1,q-1))

message = pow(c,d,n)
assert pow(message,e,n)==c
print(message)
print(hex(message))
print(binascii.a2b_hex(hex(message)[2:]))
