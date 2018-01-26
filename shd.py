# using the following line of code to fetch console input

t = int(input())
while t:
    def getleast(h):
        if h == d:
            return 1
        else:
            min = 1111111
            for i, j in con:
                dis = 11111111
                if i == h:
                    dis = 1 + getleast(j)
                elif j == h:
                    dis = 1 + getleast(i)
                if dis and dis < min:
                    min = dis
            return min
    n = int(input())
    e = int(input())
    s = int(input())
    d = int(input())
    con = list()
    for i in range(e):
        con.append(tuple(map(int, input().strip().split())))
    print(con)
    count = 0
    print(getleast(s))
    t -= 1
