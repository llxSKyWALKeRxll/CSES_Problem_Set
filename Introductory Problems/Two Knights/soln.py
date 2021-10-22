import sys,os.path
if os.path.exists('ip.in'):
    sys.stdin = open('ip.in', 'r')
    sys.stdout = open('op.out', 'w')

def detri():
	n = int(input())
	for i in range(1, n+1):
		print((i**2*(i**2-1)//2)-(4*(i-1)*(i-2)))

if __name__ == "__main__":
	detri()