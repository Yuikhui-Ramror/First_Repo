#Fibonacci sequence of n(input) iterations

def Fibonacci(n):
    a = 0
    b = 1
    for number in range(n):
        print(a)
        temp = a
        a = b
        b += temp
    
Fibonacci(int(input("Enter number of iterations of Fibonacci sequence: ")))