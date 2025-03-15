

class daily:
    def __init__(self,c):
        self.y=c[0]
        self.m=c[1]
        self.d=c[2]
        self.week=["일","월","화","수","목","금","토"]
        self.mon=[31,28,31,30,31,30,31,31,30,31,30,31]
        self.cnt=0
        self.totalD=0


    def dal(self):
        self.cnt+=(self.y-1)//4 - (self.y-1)//100 + (self.y-1)//400
        for i in range(self.m-1):
            self.cnt=self.cnt+self.mon[i]

    def TD(self):
        self.totalD=(self.y-1)*365 +self.cnt + self.d

    def dd(self):
        self.dal()
        self.TD()
        a=self.totalD%7
        print(self.week[a])

a=[]
for i in range(2):
    ymd=list(map(int,input().split()))
    a.append(ymd)
for i in range(2):
    first=daily(a[i])
    first.dd()


"""
2025 3 15
2008 6 21
"""