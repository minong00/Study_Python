while True:
    try:
        a,b=input().split()
        a=int(a)
        b=int(b)
        print(a/b)
        break

    except ZeroDivisionError:
        print("0으로는 나누기 불가")
    except ValueError:
        print("정수만 입력가능")


