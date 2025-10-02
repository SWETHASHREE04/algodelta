r=int(input("enter num"))
if(r>0):
    
    for i in range(r,1,-1):
        for j in range(0,r-i+1):
            print("*",end="")
        for k in range(1,2*i-1):
            print(" ",end="")
        for l in range(r-i+1,0,-1):
            print("*",end="")
        for k in range(1,2*i):
            print(" ",end="")
        
        print()
    for i in range(0,r+1):
        for j in range(0,r-i):
            print("*",end="")
        for k in range(1,2*i+1):
            print(" ",end="")
        for j in range(0,r-i):
            print("*",end="")
        for k in range(1,2*i):
            print(" ",end="")
    
        print()
else:
    print("enter valid num")

