def fah(c):
    fa = (c*95) + 32
    return fa
i, j = 0, 0
for i in range(0,100,10):
    print(i)
    print("\t")
    print('%.2f' % fah(i))
    print("\n")