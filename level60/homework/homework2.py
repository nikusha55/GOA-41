def sum_digits(number):
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number