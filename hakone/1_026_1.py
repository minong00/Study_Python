a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
print (a[1]*4)#a의 1번값에 4곱함
print (a*4)#a를 4번 출력


t=['a','b','c','d','e']

print(t[1:3])#1부터 2까지
print(t[1:])#1부터 끝ㄲㅏ지
print(t[:3])#처음부터 2까지
print(t[:])#전체

t[1:3]=['x','y']# 1~2를 x,t로 바꿈
print(t)

t.extend(a)#t에 a를 넣어줌
print(t)

t.sort()#정렬
print(t)

x=t.pop()#맨 뒤에꺼 삭제
x=t.pop(1)#1번 삭제
#pop은 넣기 가능

del t[4]#4번제 삭ㅈㅔ
del t[1:5]#1부터 4까지
#넣기 불가

t.remove('c')#c를 다 제거
