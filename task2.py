n=int(input("enter num:"))
for i in range(1,4):
    
    for j in range (1,n*4+2):
        
        if( (i+j)%4==0 ):
            print(j,end=" ")

        else:
            if(i==2 and j%2==0):
                print(j,end=" ")
            else:
                print("  ",end=" ")
            
        
    print()