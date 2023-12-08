with open('day8.txt') as f:
    lines = f.readlines()

cmd = lines[0].strip()
print(repr(cmd))
maps = {}
for line in lines[2:]:
    maps[line[:3]] = (line[7:10],line[12:15])
    print(repr(list(maps)[-1]), maps[list(maps)[-1]])
print('======================================')



steps = 0
loops = 0
location = 'AAA'
while (True):
    loops += 1
    if loops % 10 == 0:
        print(f'Loops = {loops}')
    if loops > 100:
        raise Exception('Too many loops')
    for c in cmd:
        steps += 1
        if location == 'ZZZ':
            break
        location = maps[location][0 if c == 'L' else 1]
    if location == 'ZZZ':
        break

print('steps = ', steps)

