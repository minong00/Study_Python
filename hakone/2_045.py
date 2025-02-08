n=int(input())
map=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(0)
    map.append(row)

num=1
yy=0
xx=n//2
map[yy][xx]=num
for i in range(n):
    for j in range(n):
        xx-=1
        yy-=1
        if(xx<0):
            xx=n-1
        if(yy<0):
            yy=n-1
        if(map[yy][xx]!=0):
            xx+=1
            yy+=1
            if(xx>=n):
                xx=0
            if(yy>=n):
                yy=0
            yy+=1
        num+=1
        map[yy][xx]=num
        if(num==n*n):
            break
for a in range(n):
    print(map[a])






