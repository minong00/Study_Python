a="May i help u"
print(a.split())# 문자열이 리스트 형태로 나옴
# 스플릿 괄호 안에 아무 것도 안쓰면 공백으로 나눔

a="one,two,three"
print(a.split())

a="one\ntwo\nthree"
print(a.splitlines())# 줄별로 나눔

a="%"
print(a.join("파이썬"))

#map(함수이름, 리스트명)
a=["3", "10", "17"]
b=list(map(int, a))#리스트를 정수형으로 바꿔줌
print(b)