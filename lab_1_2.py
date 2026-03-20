import math
import random

TR = 2.0
A, B = 0.0, math.pi
TRIALS = 100  

def mc_average(n):
    total = 0.0
    for _ in range(n):
        x = random.uniform(A, B)
        total += math.sin(x)
    return (B - A) * total / n

def find_n_for_accuracy(target_accuracy):
    max_error = (1 - target_accuracy) * TR
    n = 10
    while True:
       
        success = 0
        for _ in range(TRIALS):
            approx = mc_average(n)
            if abs(approx - TR) <= max_error:
                success += 1
        
        if success / TRIALS >= 0.95:  
            final_result = mc_average(n)
            error = abs(final_result - TR)
            return n, final_result, error
        
        n = int(n * 1.5)  


random.seed(42)  
for acc in [0.9, 0.99, 0.999, 0.99999]:
    n, result, error = find_n_for_accuracy(acc)
    print(f"Точность {acc}: n={n}, результат={result:.6f}, ошибка={error:.6f}")
