numbers = 'AKQJT98765432'
def find_type(s):
    ss = set(s)
    if len(ss) == 5:
        return 1  # High card
    elif len(ss) == 4:
        return 2  # One pair
    elif len(ss) == 3:
        for i in ss:
            if s.count(i) == 3:
                return 4  # Three of a kind
        return 3  # Two pairs
    elif len(ss) == 2:
        for i in ss:
            if s.count(i) == 3:
                return 5  # Full house
        return 6  # Four of a kind
    else:
        return 7  # Five of a kind

with open('day7.txt') as f:
    lines = f.readlines()

hands = []
for line in lines:
    tmp = line.strip().split(' ')
    hands.append([tmp[0],[len(numbers) - numbers.index(x) for x in tmp[0]], int(tmp[1])])
    hands[-1].append(find_type(hands[-1][1]))
    print(hands[-1])

print('-------------')
answer = 0
for i, hand in enumerate(sorted(hands, key = lambda x: x[3]*1e10+x[1][0]*1e8+x[1][1]*1e6+x[1][2]*1e4+x[1][3]*1e2+x[1][4])):
    answer += (i+1) * hand[2]
    tmp = [i+1]
    tmp.extend(hand)
    print(tmp)

print('answer = ', answer)

