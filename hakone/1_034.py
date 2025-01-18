a={'사과':'apple','포도':'grape','수박':'watermelon'}
for key, val in a.items():
    print(key+" 는(은) "+val)


b={'대한민국':'korea','일본':'japan','미국':'america'}
while(True):
    c=input("key=? ")
    if(c=="0"):
        break
    print(b[c])
