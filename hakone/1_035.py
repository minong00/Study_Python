#튜플
#튜플은 변경XXX

#초기화
car=("소나타","그랜져")
print(car)
print(car[0])
print(car[1])

#초기화2
name = "나"
age=22
hobby="취미"
print(name,age,hobby)

#튜플로 처리
name,age,hobby=("너",21,"취")
print(name,age,hobby)

#삭제
a=(1,2,3)
b='a','b','c'
print(a)
print(b)
del(a)#전체 삭제라 가능

#응용
a=(1,2,3)
b='a','b','c'
print(a[0]+a[1]+a[2])


print(a[0:2])
print(a[1:])

print(a+b)
print(b*3)

#변경 방법
x=(1,2,3)
y=list(x)
y.append(4)
x=tuple(y)
print(x)