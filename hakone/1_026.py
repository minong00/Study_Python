a=[]
for i in range(0,3):
    a.append(input("입력? "))
for i in range(0,3):

    for j in range(0,len(a[i])):
        temp=a[i][0]
        a[i][j]=a[i][j+1]

        a[i][len(a[i])]=temp

print(a)