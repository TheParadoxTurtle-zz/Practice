from collections import deque, Counter

temp = raw_input().split()
n = int(temp[0])
m = int(temp[1])
parents = map(lambda x:int(x) - 1, raw_input().split())
children = [[] for i in range(n)]
for i in range(1, n):
    children[parents[i-1]].append(i)

characters = raw_input()
depth = [0]*n
depth[0] = 1

queue = deque([0])
while len(queue) > 0:
    v = queue.popleft()
    for i in children[v]:
        queue.append(i)
        depth[i] = depth[v] + 1

col = {}
def getLetters(v, d):
    global col
    if d < 1:
        return []
    elif (v, d) in col:
        return col[(v, d)]
    elif d == 1:
        col[(v, d)] = [characters[v]]
        return [characters[v]]
    else:
        letters = []
        for i in children[v]:
            letters += getLetters(i, d-1)
            col[(v, d)] = letters
            return letters

for i in range(0, m):
    temp = raw_input().split()
    v = int(temp[0]) - 1
    h = int(temp[1])
    letters = getLetters(v, h - depth[v] + 1)
    counts = Counter(letters)
    numOdd = 0
    for i in counts:
        numOdd += counts[i] % 2
        if numOdd > 1:
            print "No"
        else:
            print "Yes"

