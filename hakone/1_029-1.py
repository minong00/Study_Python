def life(name, age, *hobby):
    print("이름:{0},나이:{1}".format(name, age),end=" ")
    print("취미:",end="")
    for i in hobby:
        print(i,end=" ")
    print()



life("김민종",16,"게임","어")