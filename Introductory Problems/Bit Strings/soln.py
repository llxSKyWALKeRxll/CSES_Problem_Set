import sys,os.path
if os.path.exists('ip.in'):
    sys.stdin = open('ip.in', 'r')
    sys.stdout = open('op.out', 'w')

mod = int(1e9+7)

def detri():
	n = int(input())
	print(2**n%mod)

if __name__ == "__main__":
	detri()