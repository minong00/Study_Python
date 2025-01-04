a=[[4,5,6,3,2],[4,2,3,7,7],[5,7,2,6,9]]
for i in range(3):
    for j in range(5):
        print(a[i][j],end=" ")
    print()


a=[]
b=[]
cnt=1
c=[]
for o in range(0,2):
    for i in range(0,3):
        for j in range(0,3):
            c.append(cnt)
            cnt+=1
        if(cnt>10):
            b.append(c)
        else:
            a.append(c)
        c=[]
print(a)
print(b)
for i in range(0,3):
    for j in range(0,3):
        print(a[i][j]+b[i][j], end=" ")
    print()


cnt=0
ship=12
sum=0
a=[[cnt for _ in range(0,3)] for _ in range(0,4)]
for i in range(0,4):
    for j in range(0,3):
        a[i][j]=ship-cnt


        print(a[i][j],end=" ")
        sum+=a[i][j]
        cnt+=1
    print()



print(sum)
