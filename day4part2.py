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

tot_num_cards = 0
num_cards = [1]*len(cards)
for i in range(len(cards)):
    print('------- Card ', i, '---------')
    tot_num_cards += num_cards[i]
    num_matched = 0
    for mynum in cards[i][1]:
        if mynum in cards[i][0]:
            num_matched += 1
            num_cards[i+num_matched] += num_cards[i]


print('Number of cards = ', tot_num_cards)
