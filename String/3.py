def long(l):
    print(l)
    m = l[0]
    leng = len(l[0])
    for i in l:
        if len(i) > leng :
            m = i
    return m
s = input("Enter the sentence: ")
l = s.split()
ll = long(l)
print("Longest word is ", ll,"and its length is ",len(ll))