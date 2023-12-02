games = []
with open('day2part1.txt') as f:
    for line in f:
        line = line.replace('\n','')
        substr = line.split(':')
        ID = int(substr[0].replace('Game ',''))
        print(ID, ' ==> ', substr[1])
        game = []
        for substr2 in substr[1].split(';'):
            round = [0,0,0]
            for substr3 in substr2.split(', '):
                substr4 = substr3.split(' ')
                substr4 = [tmp for tmp in substr4 if tmp]
                if substr4[1] == 'blue':
                    round[0] = int(substr4[0])
                elif substr4[1] == 'green':
                    round[1] = int(substr4[0])
                elif substr4[1] == 'red':
                    round[2] = int(substr4[0])
                else:
                    raise Exception('error')
            game.append(round)
        print(game)
        games.append([ID,game])

answer = 0
for game in games:
    B = 0
    G = 0
    R = 0
    for round in game[1]:
        if round[0] > B:
            B = round[0]
        if round[1] > G:
            G = round[1]
        if round[2] > R:
            R = round[2]
    print(game[1],' ==> ',[B,G,R])
    answer += B*G*R

print('answer = ', answer)


