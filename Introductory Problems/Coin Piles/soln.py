import sys,os.path
if os.path.exists('ip.in'):
    sys.stdin = open('ip.in', 'r')
    sys.stdout = open('op.out', 'w')
 
mod = int(1e9+7)
 
def detri():
	for T in range(int(input())):
		a, b = map(int, input().split())
		if max(a,b) > min(a,b)*2: print("NO"); continue
		print("YES" if not (a+b)%3 else "NO")
 
if __name__ == "__main__":
	detri()