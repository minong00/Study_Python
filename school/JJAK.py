#개발
memo={}

def jjak(remain,sit):
    cnt=0
    key=str([remain,sit])

    if( key in memo):
        return memo[key]
    if(remain<0):
        return 0
    if (remain==0):
        return 1
    for i in range(sit,remain+1):
        if()


print(jjak(100,2))
