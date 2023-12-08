from itertools import cycle
import math

with open('day8.txt') as f:
    lines = f.readlines()

cmd = lines[0].strip()
print(repr(cmd))
maps = {}

for line in lines[2:]:
    maps[line[:3]] = {"L":line[7:10], "R":line[12:15]}
    print(line[:3], line[7:10], line[12:15])
print('======================================')

locations = [k for k in maps.keys() if k[-1] == 'A']
steps = []
for location in locations:
    for step, c in enumerate(cycle(cmd), 1):
        location = maps[location][c]
        if location[-1] == 'Z':
            steps.append(step)
            break

answer = math.lcm(*steps)
print('answer = ', answer)



