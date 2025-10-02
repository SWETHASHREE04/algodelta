a= int(input("enter num")) #r-1 2*i
for r in range (0,a):
    for i in range(0,r):
        for j in range(0,r-i):
            print(" ",end="")
        for k in range(1,2*i):
            print("*",end="")
        print()
    for i in range(r,0,-1):
        for j in range(0,r-i):
            print(" ",end="")
        for k in range(1,2*i):
            print("*",end="")
        print()

