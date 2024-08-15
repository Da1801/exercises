def sum_numbers(number):
    if number <0:
        number *= -1

    if number <10:
        return number
    
    return number%10 + sum_numbers(number //10)