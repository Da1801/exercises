def sum_numbers(n):
    n = abs(n)
    if n < 10:
        return n
        
    sum = (n % 10) + sum_numbers(n//10)
    return (n % 10) + sum_numbers(n//10)