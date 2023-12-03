numbers = ['0','1','2','3','4','5','6','7','8','9']
with open('day3part1.txt') as f:
    schm = []
    for line in f:
        schm.append(line.strip())

wx = len(schm[0])
wy = len(schm)

sym_map = []
num = []

for iy in range(wy):
    numDetected = False
    tmpnum = []
    sym_map.append('')
    for ix in range(wx):
        c = schm[iy][ix]
        sym_map[-1] = sym_map[-1] + '0'
        if c != '.':
            if c in numbers:
                if not numDetected:
                    numDetected = True
                    numStart = ix
            else:
                if numDetected:
                    numDetected = False
                    tmpnum.append([iy,numStart,ix-numStart])
                sym_map[-1] = sym_map[-1][:-1] + '1'
        elif numDetected:
            numDetected = False
            tmpnum.append([iy, numStart, ix - numStart])
    if numDetected:
        tmpnum.append([iy, numStart, ix + 1 - numStart])
    num.extend(tmpnum)
    # print('------------------------')
    # print([schm[iy]])
    # print([sym_map[iy]])
    # print(tmpnum)

print('------------------------')
answer = 0
last_n0 = -1
for n in num:
    if n[0] != last_n0:
        last_n0 = n[0]
        print('------------- line ', n[0], '-----------------')
        if (n[0] > 0):
            print(n[0]-1, ': ', [schm[n[0]-1]])
        print(n[0], ': ', [schm[n[0]]])
        if (n[0] < wy - 1):
            print(n[0]+1, ': ', [schm[n[0]+1]])
    msg = f'search for {n} ==> {[schm[n[0]][n[1]:(n[1] + n[2])]]}'
    ix1 = n[1] - 1
    ix2 = n[1] + n[2] + 1
    if ix1<0:
        ix1 = 0
    if ix2 > wx:
        ix2 = wx
    if any(x for x in sym_map[n[0]][ix1:ix2] if x == '1') \
            or (n[0] > 0 and any(x for x in sym_map[n[0] - 1][ix1:ix2] if x == '1')) \
            or (n[0] < wy - 1 and any(x for x in sym_map[n[0] + 1][ix1:ix2] if x == '1')):
        answer += int(schm[n[0]][n[1]:(n[1] + n[2])])

        msg += ' Yes! ==> ' + str(answer)
    print(msg)


print('answer = ', answer)







