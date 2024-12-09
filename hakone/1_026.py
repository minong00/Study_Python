#a=[]
#for i in range(0,3):
#    a.append(input("입력? "))
#for i in range(0,3):
#    for j in range(len(a[i])-1,-1,-1):
#        print(a[i][j],end="")
#    print()

a=[]
for i in range(0,3):
    a.append(input("입력? "))
for i in range(0,3):
    for j in range(len(a[i])-3,len(a[i])):
        print(a[i][j],end="")
    print()