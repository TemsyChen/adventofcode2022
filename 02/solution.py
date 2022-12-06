f = open('input.txt', 'r')
input = [line for line in f.readlines()]

# A, X = rock = 1
# B, Y = paper = 2
# C, Z = scissors = 3

# lose = 0 = a/z, b/x, c/y
# draw = 3 = a/x, b/y, c/z
# win = 6 = a/y, b/z, c/x

# test
# B Y = 3 + 2
# A Z = 0 + 3
# C Z = 3 + 3
# 14

'''Part 1'''
lose = ['A Z', 'B X', 'C Y']
draw = ['A X', 'B Y', 'C Z']
win = ['A Y', 'B Z', 'C X']

points = 0

for line in input:
    line = line.strip('\n')
    if line in lose:
        points += 0
    elif line in draw:
        points += 3
    else:
        points += 6

    if line[2] == 'X':
        points += 1
    elif line[2] == 'Y':
        points += 2
    else:
        points += 3

print(points)

# A = rock = 1
# B = paper = 2
# C = scissors = 3

# X = lose
# Y = draw
# Z = win

# A, X = rock = 1
# B, Y = paper = 2
# C, Z = scissors = 3

# lose = 0 = a/z, b/x, c/y
# draw = 3 = a/x, b/y, c/z
# win = 6 = a/y, b/z, c/x

'''Part 2'''
X = {'A':3, 'B':1, 'C':2}
Y = {'A':1, 'B':2, 'C':3}
Z = {'A':2, 'B':3, 'C':1}
points = 0

for line in input:
    line = line.strip('\n')

    # if line[0] in lose:
    #     points += 0
    # elif line in draw:
    #     points += 3
    # else:
    #     points += 6
    me = line[2]
    elf = line[0]

    if me == 'X':
        points += 0 + X[elf]
    elif me == 'Y':
        points += 3 + Y[elf]
    else:
        points += 6 + Z[elf]

print(points)