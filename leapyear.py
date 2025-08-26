x = int(input("Enter Year: "))

if x % 4 == 0:                 
    if x % 100 == 0:            
        if x % 400 == 0:        
            print(x, "is a Leap Year")
        else:
            print(x, "is not a Leap Year")
    else:
        print(x, "is a Leap Year")
else:
    print(x, "is not a Leap Year")
