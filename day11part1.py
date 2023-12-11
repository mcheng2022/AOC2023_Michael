with open('day11.txt') as f:
    lines = f.readlines()

universe = [i.strip() for i in lines]
for i in universe:
    print(repr(i))

# calculate expansion
row2expand = []
col2expand = []
for rowi in range(len(universe[0])):
    if all(it == '.' for it in universe[rowi]):
        row2expand.insert(0,rowi)
print('row2expand: ', row2expand)
for coli in range(len(universe)):
    if all(it[coli] == '.' for it in universe):
        col2expand.insert(0,coli)
print('col2expand: ', col2expand)

# do expansion
for i in row2expand:
    universe.insert(i,universe[i])
print('rows expanded.')
for i in universe:
    print(repr(i))
for i in col2expand:
    for j in range(len(universe)):
        universe[j] = universe[j][:i] + '.' + universe[j][i:]
print('column expanded.')
for i in universe:
    print(repr(i))

galaxyNo = []
for i in range(len(universe)):
    for j in range(len(universe[0])):
        if universe[i][j] == '#':
            galaxyNo.append([i,j])

answer = 0
for i in range(len(galaxyNo)-1):
    for j in range(i+1,len(galaxyNo)):
        answer += abs(galaxyNo[i][0]-galaxyNo[j][0]) + abs(galaxyNo[i][1]-galaxyNo[j][1])
print('answer =', answer)
