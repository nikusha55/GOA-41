def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def backwards_prime(start, stop):
    result = []
    for num in range(start, stop + 1):
        reverse_num = int(str(num)[::-1])
        if num != reverse_num and is_prime(num) and is_prime(reverse_num):
            result.append(num)
    return result
