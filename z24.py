try:
    f = open("data.txt")
except:
    print("cannot open file")
    exit()
k = 0
n = 0
for line in f:
    for i in line.split():
        if k == 0:
            n = i
            k = k + 1
        else:
            if n < i:
                k = k + 1
                n = i
            elif i < n:
                fl = 1
                print("Wrong sequence")
                f.close()
                exit()
print(k)
f.close()
