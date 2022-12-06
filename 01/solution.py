f = open('input.txt', 'r')
input = [line for line in f.readlines()]

calorie_groups = {}
elf = 0

for line in input:
    if line == '\n':
        elf += 1
    else:
        line = line.strip('\n')
        if elf not in calorie_groups:
            calorie_groups[elf] = int(line)
        else:
            calorie_groups[elf] += int(line)


max_cal = max(calorie_groups.values())

print(f'max cal: {max_cal}')

top_three = sum(sorted(list(calorie_groups.values()), reverse=True)[:3])

print(f'top three: {top_three}')


