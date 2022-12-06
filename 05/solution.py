with open('input.txt') as fp:
    input = fp.read().splitlines()

'''
PART 1
Understand
This is a 2D array
Find the index location of the characters, using ascii letters, that rep. columns
Loop through the instruction strings,
taking the first number to indicate how many time you loop the next instruction.
Next number is what column/key to pop last value from.
Last number is what key to INSERT to (can't use append because must reverse order)

Plan
Parse the input and create a dictionary with it, like this
{1: ['A','B'],
 2: ['C','D']}

Parse instruction strings
-first number is for loop iteration number
-second number is what column to pop from
-third number is what column to append to

return solution: return last char from each column
'''
from string import ascii_uppercase
from collections import defaultdict

# #Parse input, create dict
# stack_dict = defaultdict(list)

# for line in input:
#     #create the dict
#     if '[' in line: 
#         for k, v in enumerate(line):
#             if v in ascii_uppercase:
#                 k = (k//4)+1
#                 stack_dict[k].insert(0,v)
#     #follow stacking instructions
#     elif 'move' in line: 
#         move = [int(i) for i in line.split() if i.isdigit()]
#         # print(f'move: {move}')
#         for i in range(move[0]):
#             popped = stack_dict[move[1]].pop()
#             # print(f'popped: {popped}')
#             stack_dict[move[2]].append(popped)
#             # print(stack_dict)

# #return solution
# result = ''
# for k in sorted(stack_dict.keys()):
#     result = result + stack_dict[k].pop()

# print(result)

'''
PART 2
Understand
instead of move[0] being the number of iterations,
it is the length of the last values of the list to move.
'''
stack_dict = defaultdict(list)

for line in input:
    #create the dict
    if '[' in line: 
        for k, v in enumerate(line):
            if v in ascii_uppercase:
                k = (k//4)+1
                stack_dict[k].insert(0,v)
    #follow stacking instructions
    elif 'move' in line: 
        move = [int(i) for i in line.split() if i.isdigit()]
        print(f'move: {move}')
        popped = stack_dict[move[1]][-move[0]:]
        stack_dict[move[1]] = stack_dict[move[1]][:len(stack_dict[move[1]])-move[0]]
        print(f'popped: {popped}')
        for i in popped:
            stack_dict[move[2]].append(i)
        print(stack_dict)

#return solution
result = ''
for k in sorted(stack_dict.keys()):
    result = result + stack_dict[k].pop()

print(result)