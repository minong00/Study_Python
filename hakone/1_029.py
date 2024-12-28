from django.template.defaultfilters import yesno


def gcd(a,b):
    #최대공약수
    if(a<b):
        max=b
    else:
        max=a
    for i in range(max,0,-1):
        if(a%i==0 and b%i==0):
            return i

def gcd2(a,b):
    while(a%b!=0):
        z=a%b
        a=b
        b=z
    return b


a=int(input())
b=int(input())
ab=a*b
v=gcd2(a,b)
print(v)
print(ab//v)