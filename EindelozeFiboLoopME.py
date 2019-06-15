# Fibonacci

FN = [1, 1, 2, 3, 5]
def ThomasweetnietwatFibonacciis(Fibo):
    for int in FN:
        Fibo.append(Fibo[-1] + Fibo[-2])

    return Fibo
    
print(ThomasweetnietwatFibonacciis(FN))
