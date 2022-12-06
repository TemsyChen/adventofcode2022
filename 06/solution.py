with open('input.txt') as fp:
    input = fp.read()

'''
PART 1
Given a string, return the index of the string when the last 4 characters are all unique
'''

for i, char in enumerate(str(input)):
    # print(i, input[(i-14):i], set(input[(i-14):i]))
    if len(set(input[(i-14):i])) == 14:
        print(i)
        break
    else:
        continue

'''
PART 2

'''