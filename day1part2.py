numbers = ['0','1','2','3','4','5','6','7','8','9']
NUMBERS = [
    ('one',1),
    ('two',2),
    ('three',3),
    ('four',4),
    ('five',5),
    ('six',6),
    ('seven',7),
    ('eight',8),
    ('nine',9),
    ('zero',0)
]

calib = 0
with open('day1part1.txt') as f:
    for line in f:
        str = line[:-1]
        for i in range(0,len(line)):
            if line[i] in numbers:
                str += ' ==> ' + line[i]
                calib += int(line[i])*10
                break
            else:
                got_digit = False
                for NUM in NUMBERS:
                    if (len(line)-i) >= len(NUM[0]) and line[i:i+len(NUM[0])] == NUM[0]:
                        str += ' ==> ' + NUM[0]
                        calib += NUM[1]*10
                        got_digit = True
                        break
                if got_digit:
                    break

        for i in range(len(line)-1,-1,-1):
            if line[i] in numbers:
                calib += int(line[i])
                str += ',' + line[i]
                break
            else:
                got_digit = False
                for NUM in NUMBERS:
                    if (i+1) >= len(NUM[0]) and line[i+1-len(NUM[0]):i+1] == NUM[0]:
                        str += ',' + NUM[0]
                        calib += NUM[1]
                        got_digit = True
                        break
                if got_digit:
                    break
        str += f': {calib}'
        print(str)
print(f'Calibration = {calib}')