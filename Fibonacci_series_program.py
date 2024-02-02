def fibonacci_iterative(n):
    fib_series = [0,1]
    for i in range(2,n):
        next_term = fib_series[i-1] + fib_series[i-2]
        fib_series.append(next_term)
    return fib_series
n_terms = 10
result = fibonacci_iterative(n_terms)
print(f"fibonacci series:{result}")
