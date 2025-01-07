def gob(a,b):
    return a*b
a=int(input())
b=int(input())
print(gob(a,b))


def one(a):
    if(a<0):
        a=a*-1
    return a
a=int(input())
print(one(a))


def zegob(a,b):
    c=a^b
    return c
v=int(input())
b=int(input())
print(zegob(v,b))


def gcd(a,b):
    while(z!=0):
        z=a%b
        a=b
        b=z
    return b
d=int(input())
s=int(input())
print(gcd(s,d))
print(d*s/gcd(s,d))