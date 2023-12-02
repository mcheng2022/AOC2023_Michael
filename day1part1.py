numbers = ['0','1','2','3','4','5','6','7','8','9']

calib = 0
with open('day1part1.txt') as f:
    for line in f:
        str = line[:-1]
        for i in range(0,len(line)):
            if line[i] in numbers:
                str += ': ' + line[i] + ', '
                calib += int(line[i])*10
                break
        for i in range(len(line)-1,-1,-1):
            if line[i] in numbers:
                calib += int(line[i])
                str += line[i] + f': {calib}'
                break
        print(str)
print(f'Calibration = {calib}')


