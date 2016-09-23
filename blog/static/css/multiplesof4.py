def mult4(n):
    if n == 1:
        return 4
    else:
        return mult4(n-1) + 4
Towers of Hanoi
for i in range(1,10):
    print(mult4(i))