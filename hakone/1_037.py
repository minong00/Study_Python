d={"캣","독","맨","우맨"}
print(d)
d=list(d)#d를 리스트로 만들기
d=tuple(d)#d를 튜플로 만들기
d=set(d)#d를 셋으로 만들기
#딕셔너리는 밸류가 없어서 안되는거 같음

a=range(1,19)#1~18까지
print(a)#range(1,19)로 나옴
a=list(a)#list변환
print(a)#1~18까지 출력

from random import * #random다 가져오기
print(sample(a,3))#sample은 랜덤하게 뽑는거 같다.
shuffle(a)#섞어주기
print(a)
print(sample(a,3))#3개 뽑음
