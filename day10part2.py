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
twopipes = []
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
                        twopipes.append([k,l])
                        if len(path1) == 1:
                            path1.append(onestep)
                        else:
                            path2.append(onestep)
maps[path1[0][0]][path1[0][1]] = 0
maps[path1[1][0]][path1[1][1]] = 1
maps[path2[1][0]][path2[1][1]] = 1

if [0,1] in twopipes and [0,-1] in twopipes:
    replacement = '-'
elif [0,1] in twopipes and [1,0] in twopipes:
    replacement = 'F'
elif [0,1] in twopipes and [-1,0] in twopipes:
    replacement = 'L'
elif [-1,0] in twopipes and [0,-1] in twopipes:
    replacement = 'J'
elif [-1,0] in twopipes and [1,0] in twopipes:
    replacement = '|'
elif [1,0] in twopipes and [0,-1] in twopipes:
    replacement = '7'
dungeon[path1[0][0]] = dungeon[path1[0][0]].replace('S',replacement)

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

print('path1 = ', path1)
print('path2 = ', path2)

tiles = 0
for i in range(Ysize):
    flag = False
    msg = ''
    trigger = ''
    for j in range(Xsize):
        if maps[i][j] == -1:
            if flag:
                tiles += 1
                msg += '*'
            else:
                msg += ' '
        else:
            msg += dungeon[i][j]
            if dungeon[i][j] == '|':
                flag = not flag
            elif dungeon[i][j] in 'FL':
                trigger = dungeon[i][j]
            elif dungeon[i][j] in '7J':
                if (dungeon[i][j] == '7' and trigger == 'L') \
                        or (dungeon[i][j] == 'J' and trigger == 'F'):
                    flag = not flag
                trigger = ''
    print(msg)

print('answer = ', tiles)



