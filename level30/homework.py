def odd_index_sum(numbers):
    total = 0
    for index in range(len(numbers)):
        if index % 2 != 0:  
            total += numbers[index]
    return total