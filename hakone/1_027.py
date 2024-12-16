#num=[[4,5,6,3,2],[4,2,3,7,7],[5,7,2,6,9]]
#for i in range(len(num)):
#    for j in range(len(num[i])):
#        print(num[i][j],end=" ")
#    print()


#a=[[1,2,3],[4,5,6],[7,8,9]]
#b=[[10,11,12],[13,14,15],[16,17,18]]
#for i in range(3):
#    for j in range(3):
#        print(a[i][j]+b[i][j],end=" ")
#    print()


#a=input("입력=?")
#for i in range(0,len(a)):
#    if(a[i]<='a'):
#        print(a[i].lower(),end="")
#    else:
#        print(a[i].upper(),end="")


#a=input()[::-1]
#b=input()[::-1]
#c=input()[::-1]
#print(a)
#print(b)
#print(c)


#tmep=0
#max=0
#a=[]
#for i in range(5):
#    b=input()
#    a.append(b)
#for i in range(len(a)):
#    if(max<len(a[i])):
#        max=len(a[i])
#        temp=i
#print(a[temp])


#a=[]
#for i in range(3):
#    b=input("입력=? ")
#    a.append(b)
#for i in range(len(a)):
#    print(a[i][len(a[i])-3:len(a[i]):])


a=[]
for i in range(5):
    b=input()
    a.append(b)
max=a[0]
for i in range(len(a)-1):
    if(max>a[i+1]):
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp

for  i in range(len(a)):
    print(a[i])