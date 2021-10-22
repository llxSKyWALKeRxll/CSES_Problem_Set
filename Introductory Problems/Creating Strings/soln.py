import sys,os.path

if os.path.exists('ip.in'): sys.stdin = open('ip.in', 'r'); sys.stdout = open('op.out', 'w')
	
strings = []

def createStrings(s, l, r):
	if l==r:
		strings.append("".join(s))
	else:
		for i in range(l, r+1):
			s[l], s[i] = s[i], s[l]
			createStrings(s, l+1, r)
			s[l], s[i] = s[i], s[l]

def detri():
	s = input()
	createStrings(list(s), 0, len(s)-1)
	ans = sorted(list(set(strings)))
	print(len(ans))
	print(*ans, sep="\n")

if __name__ == "__main__":
	detri()