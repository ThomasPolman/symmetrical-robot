# Fibonacci

def ThomasweetnietwatFibonacciis(Fibo):
    
    for FN in range(50):
        Fibo.append(Fibo[-1] + Fibo[-2])

    return Fibo
    
print(ThomasweetnietwatFibonacciis([1, 1, 2, 3, 5]))
