try:
    f = open("data.txt")
except:
    print("cannot open file")
k = 0
n = 0
fl = 0
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
if fl==0:
    print(k)
else:
    print("Wrong sequence")
f.close()
