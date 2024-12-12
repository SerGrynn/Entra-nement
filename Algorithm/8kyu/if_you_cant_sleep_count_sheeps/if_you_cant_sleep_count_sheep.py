def count_sheep(n):
    # your code
    i = 0
    sheep= ""
    if n == 0:
        return ("")
    while i != n:
        i = i + 1
        sheep += f"{i} sheep..."
    return sheep
print(count_sheep(2))