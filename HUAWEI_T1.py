import collections
score = int(input())
problems = [2]*10+[4]*10+[8]*5
hash = collections.defaultdict(list)
# dp = [[0] for _ in range(25) for _ in range(4)]
_sum = 0 
for i in range(25):
    hash[(i, 0)].append( _sum + problems[i])
    _sum = _sum + problems[i]
hash[(0,1)] = [0]
hash[(0,2)] = [0]
hash[(0,3)] = [0]
for i in range(1, 25):
    
    hash[(i,1)] = [s+problems[i] for s in hash[(i-1, 1)]] + hash[(i-1, 0)]
    hash[(i,2)] = hash[(i-1, 1)]+[s+problems[i] for s in hash[(i-1, 2)]]
    hash[(i,3)] = hash[(i-1, 2)]+[s+problems[i] for s in hash[(i-1, 2)]]
cnt = 0
for k in hash[(24,3)]+hash[(24,0)]:
    if k == score:
        cnt += 1
print(cnt)


