import math
TT = [7, 15, 30]
DD = [9, 40, 200]

TT = [ 48  ,   87   ,  69  ,   81]
DD = [255   ,1288  , 1117  , 1623]

TT = [71530]
DD = [940200]

TT = [48876981]
DD = [255128811171623]

answer = 1
for T, D in zip(TT, DD):
    print('Time,Dist = ', T, ',', D)
    t = math.sqrt(T**2-4*D)
    t1 = T/2 - t/2
    t2 = T/2 + t/2
    t1 = int(1 if t1 < 1 else math.ceil(t1))
    t2 = int(T - 1 if t2 >= int(T) else math.floor(t2))
    if t1*(int(T)-t1) == int(D):
        t1 += 1
    if t2*(int(T)-t2) == int(D):
        t2 -= 1
    print('t,t1,t2, num = ', [t, t1, t2, t2-t1+1])
    answer *= t2 - t1 + 1

print('answer = ', answer)




