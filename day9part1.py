with open('day9.txt') as f:
    lines = f.readlines()

records = []
for line in lines:
    records.append([[int(i) for i in line.strip().split(' ')]])

print('records: ', records)

for i in range(len(records)):
    print('------', i, '------')
    while True:
        print(records[i][-1])
        records[i].append([records[i][-1][t + 1] - records[i][-1][t] for t in range(len(records[i][-1])-1)])
        if not any(records[i][-1]):
            records[i][-1].pop()
            break

answer = 0
for r in records:
    for i in range(len(r)):
        answer += r[i][-1]

print('answer = ', answer)

