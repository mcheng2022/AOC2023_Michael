with open('day8_example3.txt') as f:
    lines = f.readlines()

cmd = lines[0].strip()
print(repr(cmd))
N = []
L = []
R = []
for line in lines[2:]:
    N.append(line[:3])
    L.append(line[7:10])
    R.append(line[12:15])
    print(N[-1], L[-1], R[-1])
L = [N.index(i) for i in L]
R = [N.index(i) for i in R]
N2 = [s[2] == 'Z' for s in N]
print('======================================')
locations = [i for i, s in enumerate(N) if s[2] == 'A']
print([N[i] for i in locations])

steps = 0
loops = 0
while (True):
    # loops += 1
    # if loops % 10000000 == 0:
    #     print(f'Loops = {loops}')
    # if loops > 10:
    #     raise Exception('Too many loops')
    for c in cmd:
        # print('locations: ', [N[i] for i in locations], ', c = ', c)
        steps += 1
        if c == 'L':
            locations = [L[i] for i in locations]
        else:
            locations = [R[i] for i in locations]
    if all(N2[i] for i in locations):
        # print('locations: ', [N[i] for i in locations], ', c = ', c)
        break

print('steps = ', steps)

