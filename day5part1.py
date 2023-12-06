with open('day5.txt') as f:
    lines = f.readlines()

# get seeds
num = [int(x) for x in lines[0].strip().split(':')[1].split(' ') if x]
print('initial numbers: ', num)
LineID = 1
while(LineID < len(lines)-1):
    print('--------------------------------------------------')
    while(LineID < len(lines)-1):
        if ':' in lines[LineID := LineID + 1]:
            print('[',lines[LineID].strip().split(':')[0],']')
            break
    mapping = []
    while(LineID < len(lines)-1):
        LineID += 1
        tmpmap = [int(x) for x in lines[LineID].strip().split(' ') if x]
        if len(tmpmap) == 0:
            break
        mapping.append(tmpmap)
    print('get mapping: ', mapping)
    newnum = num.copy()
    for m in mapping:
        for i in range(len(num)):
            if 0 <= num[i] - m[1] < m[2]:
                newnum[i] = m[0] + (num[i] - m[1])
    num = newnum.copy()
    print('update numbers: ', num)

print('answer: ', min(num))




