import sys,os.path
if os.path.exists('ip.in'):
    sys.stdin = open('ip.in', 'r')
    sys.stdout = open('op.out', 'w')

mod = int(1e9+7)

def detri():
	n = int(input())
	ans = 0
	while n >= 5:
		n //= 5
		ans += n
	print(ans)

if __name__ == "__main__":
	detri()