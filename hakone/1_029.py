def Max(a,b):
    #최대공약수
    if(a<b):
        max=b
    else:
        max=a
    for i in range(max,1,-1):
        if(a%i==0 and b%i==0):
            return i

def Min(a,b):
    i=2
    while(True):
        a=a//i
        print(a)
        b=b//i
        print(b)
        if(a//i==0 or b//i==0):
            return a*b*i

        i=i+1

a=2
b=15
print(Min(a,b))