
with open("input.txt") as fp:
    input = fp.read().splitlines()

'''
PART 1
Understand
how many pairs does one range fully contain the other?
the min of one pair is higher than the min of the other pair, 
and the max of that pair is lower than the max of the other pair

Plan
Tally if min(A) >= min(B) and max(A) <= max(B) or vice versa
use 2D arrays
'''
# counter = 0

# for line in input:
#     p = [x.split('-') for x in line.split(',')]
#     p = [[int(x) for x in row] for row in p]
#     # print(p)
#     # print(type(p[0][0]))
#     if p[0][0] <= p[1][0] and p[0][1] >= p[1][1]:
#         counter += 1
#         print(p[0][0], p[1][0], p[0][1], p[1][1])
#     elif p[0][0] >= p[1][0] and p[0][1] <= p[1][1]:
#         counter += 1
#         print(p[0][0], p[1][0], p[0][1], p[1][1])
# print(counter)

'''
PART 2
Understand
How many pairs overlap ranges?
max(A) < min(B) or max(B) < min(A)

Plan
all else is considered overlap
'''
counter = 0

for line in input:
    p = [x.split('-') for x in line.split(',')] #create 2d array of pairs
    p = [[int(x) for x in row] for row in p] #convert value type from str to int
    print(p)
    # print(type(p[0][0]))
    if p[0][0] <= p[1][0] <= p[0][1] or p[1][0] <= p[0][0] <= p[1][1]:
        counter += 1
        print(counter)

print(counter)

#Other solutions used issubset()
total = 0
for item in assignments:
    zone_list = item.split(",")
    first_elf = set(list(map(lambda x: range(int(x[0]),int(x[1])+1),        
    [item.split("-") for item in zone_list]))[0])
    second_elf = set(list(map(lambda x: range(int(x[0]),int(x[1])+1), 
    [item.split("-") for item in zone_list]))[1])
    if first_elf.issubset(second_elf) or 
    second_elf.issubset(first_elf):
        total+=1