def square_sum(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2
    return sum(numbers)
square_sum([0,3,4,5])