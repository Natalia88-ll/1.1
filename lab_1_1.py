import math

TR = 2.0
A, B = 0.0, math.pi

def rectangle_method(n):
    
    h = (B - A) / n
    total = 0.0
    for i in range(n):
        x = A + (i + 0.5) * h  
        total += math.sin(x)
    return h * total

def find_n_for_accuracy(target_accuracy):
    
    max_error = (1 - target_accuracy) * TR
    n = 1
    while True:
        approx = rectangle_method(n)
        error = abs(approx - TR)
        if error <= max_error:
            return n, approx, error
        n *= 2  


for acc in [0.9, 0.99, 0.999, 0.99999]:
    n, result, error = find_n_for_accuracy(acc)
    print(f"Точность {acc}: n={n}, результат={result:.6f}, ошибка={error:.6f}")
