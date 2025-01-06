"""
#지역
def aw():
    a=10
def main():
    a=2
    print(a)
    aw()
    print(a)
#전역
b=10
def aww():
    print(b)

def main():
    print(b)
main()
b=b+1
print(b)
"""

def weight(s,h):
    n=h/100
    if(s=="남자"):
        w=n*n*22


    else:
        w = n * n * 21
    print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다".format(s,h,round(w,2)))

h=int(input("신장을 cm로 입력: "))

s=input("성별: ")
weight(s,h)
