def pibo(n):
    #1=1
    #2=1
    #3=2
    #4=3
    #5=5
    #6=8
    #7=13
    if(n==1):
        return 1
    if(n==2):
        return 1
    else:
        return pibo(n-1)+pibo(n-2)


print(pibo(7))