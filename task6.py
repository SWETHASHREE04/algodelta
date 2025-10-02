a=int(input("enter a num"))
if(a>0):
    
    for i in range(0,a+1):
       
        for k in range (i,0,-1):
            for p in range(k,0,-1):
                print(" ",end="")
            
            for l in range(0,i):
                print("*",end="  ")
            print()
        print()



else:
    print("enter a valid num")

