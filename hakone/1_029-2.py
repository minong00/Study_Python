#filter사용
def even(n):
    if(n%2==0):
        return True
    else:
        return False
list_num=[3,5,6,8,9,12,7]

for i in filter(even,list_num):
    print(i)
#filter에서 lambda사용
list_num=[3,5,6,8,9,12,7]

for i in filter(lambda x :x%2==0,list_num):
    print(i)
#map에서 lambda사용
list_num=[3,5,6,8,9,12,7]

power=map(lambda x:x**2,list_num)

for i in power:
    print(i,end=" ")