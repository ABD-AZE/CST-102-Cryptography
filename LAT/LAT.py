def y1(x):
    x1=int(x[0:1])
    x2=int(x[1:2])
    x3=int(x[2:3])
    x4=int(x[3:4])
    y=(x1&x2&x4)^(x1&x3&x4)^(x2&x3&x4)^(x1)^(x2&x3)^(x3)^(x4)^1
    return y

def y2(x):
    x1=int(x[0:1])
    x2=int(x[1:2])
    x3=int(x[2:3])
    x4=int(x[3:4])

    y=(x1&x2&x4)^(x1&x3&x4)^(x1&x3)^(x1&x4)^(x1)^(x2)^(x3&x4)^1
    return y

def y3(x):
    x1=int(x[0:1])
    x2=int(x[1:2])
    x3=int(x[2:3])
    x4=int(x[3:4])

    y=(x1&x2&x4)^(x1&x2)^(x1&x3&x4)^(x1&x3)^(x1)^(x2&x3&x4)^(x3)
    return y

def y4(x):
    x1=int(x[0:1])
    x2=int(x[1:2])
    x3=int(x[2:3])
    x4=int(x[3:4])

    y=(x1)^(x2&x3)^(x2)^(x4)
    return y

LAT = [[0 for _ in range(16)] for _ in range(16)]
for bo in range(16):
    for ao in range(16):
        for xo in range(16):
            a=bin(ao)[2:].zfill(4)
            b=bin(bo)[2:].zfill(4)
            a1=int(a[0:1])
            a2=int(a[1:2])
            a3=int(a[2:3])
            a4=int(a[3:4])
            b1=int(b[0:1])
            b2=int(b[1:2])
            b3=int(b[2:3])
            b4=int(b[3:4])
            t=bin(xo)[2:].zfill(4)
            y1_val = y1(t)*b1
            y2_val = y2(t)*b2
            y3_val = y3(t)*b3
            y4_val = y4(t)*b4
            y_val=(y1_val<<3)+(y2_val<<2)+(y3_val<<1)+y4_val
            x1=((xo>>3)&1)*a1
            x2=((xo>>2)&1)*a2
            x3=((xo>>1)&1)*a3
            x4=(xo&1)*a4
            if(x1^x2^x3^x4^y1_val^y2_val^y3_val^y4_val==0):
                LAT[ao][bo]+=1

for i in range(16):
    for j in range(16):
        print(LAT[i][j], end=' ')
    print()

max_val = max(max(row) for row in LAT)
min_val = min(min(row) for row in LAT)
print("Maximum value:", max_val)
print("Minimum value:", min_val)

