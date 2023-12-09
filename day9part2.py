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
            records[i].pop()
            break

answer = 0
for ri, r in enumerate(records):
    print('------', ri, '------')
    sub_sum = 0
    for i in range(len(r)):
        contribute = r[i][0]*(-1)**i
        print(r[i], ': ', contribute)
        sub_sum += contribute
        answer += contribute
    print('sub_sum = ', sub_sum)

print('answer = ', answer)
