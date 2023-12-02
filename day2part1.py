
answer = 0
with open('day1part2.txt') as f:
    for line in f:
        tmp = line.split(':')
        ID = int(tmp[0].replace('Game ',''))
        print(line, ID)


