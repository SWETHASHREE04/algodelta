r= int(input("enter num"))
b = 1
for a in range(0,r):
    for i in range(1,4):
        for j in range(0,4-i):
            print(" ",end=" ")
        for k in range(1,2*i):  
            if(k==1 or k==2*i-1):
                print(b,end=" ")
                b+=1
            else:
                print(" ",end=" ")
        print()
        a+=1
        
        