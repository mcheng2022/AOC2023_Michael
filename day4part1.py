cards = []
with open('day4.txt') as f:
    for line in f:
        line = line.strip()
        tmp = line.split(':')
        print('--------------------------------------------------------')
        print(line)
        print(tmp)
        tmp2 = tmp[1].split('|')
        print(tmp2)
        tmp3 = [int(x) for x in tmp2[0].split(' ') if x]
        tmp4 = [int(x) for x in tmp2[1].split(' ') if x]
        print(tmp3)
        print(tmp4)
        cards.append([tmp3,tmp4])

print('Data Parsed! \n\n\n')

points = 0
for crd in cards:
    print('------- New Card ---------')
    pt = 0.5
    print(crd)
    for mynum in crd[1]:
        msg = 'check ' + str(mynum)
        if mynum in crd[0]:
            pt *= 2
            msg += ' ...Yes'
        print(msg)
    if pt != 0.5:
        points += int(pt)

print('points = ', points)
