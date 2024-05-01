def a_dog_walk(dog_walk):
    North_South = 0
    East_West = 0
    if len(dog_walk) != 10:
        return False
    for i in range(0, 10):  # Fix range to include the 10th element
        if dog_walk[i] == 'n':
            North_South += 1
        elif dog_walk[i] == 's':
            North_South -= 1
        elif dog_walk[i] == 'e':
            East_West += 1
        elif dog_walk[i] == 'w':
            East_West -= 1  # Fix typo, should be subtraction, not assignment
    if North_South == 0 and East_West == 0:
        return True
    return False
print(a_dog_walk(['n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 's']))