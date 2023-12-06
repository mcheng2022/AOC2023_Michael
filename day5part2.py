with open('day5.txt') as f:
    lines = f.readlines()

# get seeds
num = [int(x) for x in lines[0].strip().split(':')[1].split(' ') if x]
newnum = []
for i in range(len(num)//2):
    newnum.append(range(num[2*i],num[2*i]+num[2*i+1]))
num = newnum.copy()

# num = [range(n,n+1) for n in num]

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
        tmp = [int(x) for x in lines[LineID].strip().split(' ') if x]
        if len(tmp) == 0:
            break
        mapping.append([range(tmp[0], tmp[0] + tmp[2]), range(tmp[1], tmp[1] + tmp[2])])  # dst, src
    print('get mapping: \n', mapping)
    converted = []
    for n in num:
        unconverted = [n]
        print(f'\n >>>> num: {n}')
        for m in mapping:
            print(f' >> mapping: {m}, unconverted: {unconverted}')
            d = m[0]  # dst
            s = m[1]  # src
            updated_unconverted = []
            updated_converted = []
            for u in unconverted:
                if u[-1] < s[0] or s[-1] < u[0]:
                    print('out of range')
                    updated_unconverted.append(u)
                    continue  # no overlap
                if u[0] < s[0]:
                    print('cut front part')
                    updated_unconverted.append(range(u[0], s[0]))
                    u = range(s[0], u[-1] + 1)
                if u[-1] > s[-1]:
                    print('cut back part')
                    updated_unconverted.append(range(s[-1] + 1, u[-1] + 1))
                    u = range(u[0], s[-1] + 1)
                updated_converted.append(range(u[0] - s[0] + d[0], u[-1] - s[0] + d[0] + 1))
            unconverted = updated_unconverted.copy()
            converted.extend(updated_converted)
            print(f'converted: {updated_converted}, rest: {unconverted}')
            if not unconverted:
                print('skip rest mapping')
                break
        converted.extend(unconverted)
    num = converted.copy()
    print('new numbers: \n', num)

min_num = 9e15
for n in num:
    if n[0] < min_num:
        min_num = n[0]

print('answer: ', min_num)



