

def s(n, k, amts):
	t = 3**k
	if t < 1:
		return
	if t > n:
		s(n, k-1, amts)
	elif 2*t > n:
		amts[k] = amts[k] + 1
		s(n - t, k-1, amts)
	else:
		amts[k] = amts[k] - 1
		amts[k+1] = amts[k+1] + 1
		s(n - 2*t, k-1, amts)

def cleanup(amts):
	for i in range(0, len(amts)):
		if amts[i] == -1:
			amts[i] = 'l'
		elif amts[i] == 0:
			amts[i] = '-'
		elif amts[i] == 1:
			amts[i] = 'r'
		elif amts[i] == 2:
			amts[i] = 'l'
			amts[i+1] = amts[i+1] + 1

def solve(n):
	t = 0
	v = 1
	while v < n:
		v *= 3
		t += 1
	amts = [0 for i in range(t+1)]
	s(n, t, amts)
	cleanup(amts)
	if amts[-1] == '-':
		amts.pop()
	print n
	print amts

solve(10)
solve(8)
solve(5)

