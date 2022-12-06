import string

with open('input.txt', 'r') as file:
    input = file.read().split('\n')

'''
PART 1
Understand
find the letter that appears in both compartments 
comp 1 has first half of string, comp 2 has second half
upper and lower case matters

assign lower case letters value 1 - 26 (dict), upper 27-52

add the value of the key if it appears in first half and second half

Plan
-create a dict with letters and values
-divide string into comp1 and comp2
-check for the common char in both comps
-add values of the common char, return sum
'''

#create a dict with letters and value
az = string.ascii_lowercase + string.ascii_uppercase

az_dict = {}
value = 1
for char in az:
    az_dict[char] = value
    value += 1

#divide string into first half and second half
score = 0
for line in input:
    if len(line)%2==0: #check all lines are even
        first_half = int(len(line)/2) #better sol: len(line)//2
        comp1 = line[:first_half]
        comp2 = line[first_half:]

#check for the common char in both comps, add value of letter
    for char in comp1:
        if char in comp2:
            score += az_dict[char]
            break #won't identify the same char twice

print(score)

#better sol
total = 0
from string import ascii_letters
for line in input:
    half = len(line)//2
    left, right = line[:half], line[half:]
    common = set(left).intersection(set(right))
    try:
        total += ascii_letters.index(common.pop())+1
    except:
        continue
print(total)

'''
PART 2
Understand
find common item type b/w all 3 elves
Every 3 lines is a group
identify the common char in all 3 elves per group
add the values of the common char from all groups

Plan
-split groups to a dict of each group is a list of 3 lines
-search for the common char in each group (for loop, if char in both str)
-sum up the common char for each group
-dict will look like this:
{
    group1: [str1, str2, str3]
}
'''
from collections import defaultdict

score2 = 0

#split groups to a dict of each group is a list of 3 lines
group_dict = defaultdict(list)
group_id = 0
for line in input:
    if len(group_dict[group_id]) < 3:
        group_dict[group_id].append(line)
    else:
        group_dict[group_id+1].append(line)
        group_id += 1

#search for the common char in each group
for k,v in group_dict.items():
    for char in v[0]:
        if char in v[1] and char in v[2]:
            score2 += az_dict[char]
            break

print(score2)

#bettersol:
total = 0
for x in range(0, len(input) - 1, 3):
    group = input[x:x+3]
    common = set(group[0]).intersection(group[1]).intersection(group[2])
    total += ascii_letters.index(common.pop()) + 1
print(total)
