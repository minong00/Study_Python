def factor(n):
    output = 1
    if( n == 0):
        return 1
    else:
        return n*factor(n-1)

print(factor(5))