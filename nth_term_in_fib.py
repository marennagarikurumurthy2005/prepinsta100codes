
 # FIB using loop   
""" 
a, b = 0, 1
n = int(input("Number: "))

if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    print(c)
 """

# fib using recursion

def fib(num):
    if num<2:
        return num
    else:

        return fib(num-1)+fib(num-2)
print(fib(5))
