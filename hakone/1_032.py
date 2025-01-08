#readlines는 1차원 리스트로 나옴
#readline은 한줄만
fhand=open("input_032_prob_01.txt")

cnt=0
while True:
    line=fhand.readline()
    if(not line):
        break
    print(line,end="")
    cnt=cnt+1
print()
print("line : {0}".format(cnt))
fhand.close()