#딧셔너리는 "어쩌고:어쩌고"이게 중괄호 안에 있어야된다
#즉 키와 밸류가 같이 있어야 되는데 set은 키만 있어서
#딕셔너리랑 셋을 구분 가능거 같다.

#set 사용하기  중복ㄴㄴ, 순서X
#초기화
a={1,2,3,4,4,5,5,7}
print(a)
b=set(["반티","어쩔","티비","응","응"])#셋 안에 ㅇ리스트
print(b)

c={1,2,3,4,5}
d={1,3,5,7,9}
print(c&d)#교집합
print(c|d)#합집합
print(c-d)#차집합
print(c^d)#대칭 차집합

c.add(14)#추가
print(c)
d.remove(3)#제거
print(d)