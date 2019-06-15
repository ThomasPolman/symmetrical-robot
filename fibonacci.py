# Fibonacci

def ThomasweetnietwatFibonacciis(Fibo):
    Fibo.append(Fibo[-1] + Fibo[-2])
    Fibo.append(Fibo[-1] + Fibo[-2])
    Fibo.append(Fibo[-1] + Fibo[-2])
    Fibo.append(Fibo[-1] + Fibo[-2])
    return Fibo
    
print(ThomasweetnietwatFibonacciis([1, 1, 2, 3, 5]))
