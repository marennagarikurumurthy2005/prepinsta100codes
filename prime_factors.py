import math
while True:

    

    
    num=int(input("Enter number:"))

    factorlist=[]
    for i in range(1,num):
        if num%i==0:
            factorlist.append(i)
    print(factorlist)
    for x in factorlist:
        if x ==2:
            print(x)
        elif x>2:
            for m in range(2,x):
                if x%m==0:
                    break
            else:
                print(x)




               

    
        

        
        

        

        
        
        