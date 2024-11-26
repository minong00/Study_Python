def factor(n):
    output = 1
    while n!=1:
       output=n*output
       n=n-1

    return output

print(factor(5))
