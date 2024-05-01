def a_dog_walk(dog_walk):
    North_South = 0
    East_West = 0
    if len(dog_walk) != 10:
        return False
    for i in range(0, 9):
        if dog_walk == 'n':
            North_South += 1
        elif dog_walk == 's':
            North_South -= 1
        if dog_walk == 'e':
            East_West += 1
        elif dog_walk == 'w':
            East_West = - 1
    if North_South == 0 and East_West == 0:
        return True
print(a_dog_walk(['n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 's']))