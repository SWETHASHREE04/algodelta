"""n=int(input("enternum:"))
for i in range(1,n+1):
    for j in range(1,i):
        print(j,end="")
    print()
for i in range(n+1,1,-1):
    for j in range(1,i):
        print(j,end="")
    print()
1
12
123
1234
123S
12
1 """
r= int(input("enter num")) #r-1 2*i
if(r>0):
    for i in range(r-1,0,-1):
        for j in range(0,r-i):
            print(" ",end="")
        for k in range(1,i+2):
            print(k,end="")
        print()
    for i in range(0,r):
        for j in range(0,r-i):
            print(" ",end="")
        for k in range(1,i+2):
            print(k,end="")
        print()
else:
    print("enter a valid number")