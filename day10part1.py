with open('day10.txt') as f:
    lines = f.readlines()

dungeon = []
for line in lines:
    dungeon.append(line.strip())

cmd = [
    [[-1, 0],'7',[ 0,-1]],  # go up -> go left
    [[-1, 0],'|',[-1, 0]],  # go up -> go up
    [[-1, 0],'F',[ 0, 1]],  # go up -> go right
    [[ 1, 0],'J',[ 0,-1]],  # go down -> go left
    [[ 1, 0],'|',[ 1, 0]],  # go down -> go down
    [[ 1, 0],'L',[ 0, 1]],  # go down -> go right
    [[ 0,-1],'F',[ 1, 0]],  # go left -> go down
    [[ 0,-1],'-',[ 0,-1]],  # go left -> go left
    [[ 0,-1],'L',[-1, 0]],  # go left -> go up
    [[ 0, 1],'7',[ 1, 0]],  # go right -> go down
    [[ 0, 1],'-',[ 0, 1]],  # go right -> go right
    [[ 0, 1],'J',[-1, 0]],  # go right -> go up
]

Ysize = len(dungeon)
Xsize = len(dungeon[0])

maps = []
path1 = []
path2 = []
for i in range(Ysize):
    maps.append([-1]*Xsize)
    for j in range(Xsize):
        if dungeon[i][j] == 'S':
            path1.append([i,j])
            path2.append([i,j])
            print('star_position = ', [i,j])
            for k,l in zip([-1,1,0,0],[0,0,-1,1]):
                onestep = [i+k, j+l]
                if Ysize <= onestep[0] or onestep[0] < 0 or Xsize <= onestep[1] or onestep[1] < 0:
                    continue
                for c in cmd:
                    if [k,l] == c[0] and dungeon[onestep[0]][onestep[1]] == c[1]:
                        if len(path1) == 1:
                            path1.append(onestep)
                        else:
                            path2.append(onestep)
maps[path1[0][0]][path1[0][1]] = 0
maps[path1[1][0]][path1[1][1]] = 1
maps[path2[1][0]][path2[1][1]] = 1
print('path1&2 = ', path1, ', ', path2)

loop = 0
while True:
    loop += 1
    if loop > 1e4:
        raise Exception('Too many loops.')
    if not (path1[-1] or path2[-1]):
        break
    for c in cmd:
        if path1[-1] and \
                [path1[-1][0]-path1[-2][0],path1[-1][1]-path1[-2][1]] == c[0] and \
                    dungeon[path1[-1][0]][path1[-1][1]] == c[1]:
            path1.append([path1[-1][0] + c[2][0], path1[-1][1] + c[2][1]])
            if maps[path1[-1][0]][path1[-1][1]] == -1:
                maps[path1[-1][0]][path1[-1][1]] = maps[path1[-2][0]][path1[-2][1]] + 1
            else:
                path1[-1] = []
            break
    for c in cmd:
        if path2[-1] and \
                [path2[-1][0]-path2[-2][0],path2[-1][1]-path2[-2][1]] == c[0] and \
                    dungeon[path2[-1][0]][path2[-1][1]] == c[1]:
            path2.append([path2[-1][0] + c[2][0], path2[-1][1] + c[2][1]])
            if maps[path2[-1][0]][path2[-1][1]] == -1:
                maps[path2[-1][0]][path2[-1][1]] = maps[path2[-2][0]][path2[-2][1]] + 1
            else:
                path2[-1] = []
            break

for i in range(Ysize):
    msg = ''
    for j in range(Xsize):
        msg = msg + ('+' if maps[i][j] != -1 else '#')
    print(msg)

if not path1[-1]:
    path1.pop()
if not path2[-1]:
    path2.pop()

if len(path1) > len(path2):
    answer = len(path1) - 1
else:
    answer = len(path2) - 1

print('answer = ', answer)



