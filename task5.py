a=int(input("emter a num"))
if(a>0):
    #a= int(input("enter num")) #r-1 2*i
    for r in range (0,a+1):
        for i in range(0,r):
            for j in range(0,r-i):
                print(" ",end="")
            for k in range(1,i+1):
                print("*",end=" ")
            print()
        for i in range(r,0,-1):
            for j in range(0,r-i):
                print(" ",end="")
            for k in range(1,i+1):
                print("*",end=" ")
            print()



else:
    print("enter a valid num")

