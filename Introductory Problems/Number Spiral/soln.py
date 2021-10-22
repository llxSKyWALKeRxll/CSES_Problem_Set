import sys,os.path
if os.path.exists('ip.in'):
    sys.stdin = open('ip.in', 'r')
    sys.stdout = open('op.out', 'w')

def detri():
	for T in range(int(input())):
		y,x = map(int, input().split())
		if y>=x:
			if not y&1:
				print(y**2-(x-1))
			else:
				print((y-1)**2+x)
		else:
			if not x&1:
				print((x-1)**2+y)
			else:
				print(x**2-(y-1))


if __name__ == "__main__":
	detri()