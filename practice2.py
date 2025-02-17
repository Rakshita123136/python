t = int(input())
while t != 0:
    n, k = map(int, input().split())
    s = input()
    max_str = ""
    p = -1
    for i in range(n):
        if max_str < s:
            max_str = s
            d = i
        elif max_str == s:
            p = i - d
            break
        s = s[1:] + s[0]

    if p == -1:
        print(d + (k - 1) * n)
    else:
        print(d + (k - 1) * p)
    print(" ")
    t -= 1
