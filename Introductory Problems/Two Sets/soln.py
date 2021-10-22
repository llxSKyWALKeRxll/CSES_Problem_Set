import sys,os.path
if os.path.exists('ip.in'):
    sys.stdin = open('ip.in', 'r')
    sys.stdout = open('op.out', 'w')

def detri():
	n = int(input()) 
	if (n*(n+1))%4:
		print("NO")
	else:
		l1, l2 = [], []
		i = 1
		if n%4:
			l1.append(1); l1.append(2); l2.append(3)
			i = 4
		while i<=n:
				l1.append(i); l1.append(i+3); l2.append(i+1); l2.append(i+2)
				i += 4
		print("YES")
		print(len(l1), *l1)
		print(len(l2), *l2)

if __name__ == "__main__":
	detri() 