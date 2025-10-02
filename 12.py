a=int(input("enter a num"))
if(a>0):
    
    for i in range(1,a+2):
        
       for j in range(1,a*2+1):
           for k in range(a*2+1,1,-1):
                if(k==1 or k==a*2+1):
                    print(j,end="")
                else:
                    print(" ",end="")
       print()

else:
    print("enter a valid num")

