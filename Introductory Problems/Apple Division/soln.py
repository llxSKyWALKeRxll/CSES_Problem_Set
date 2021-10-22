import sys,os.path

if os.path.exists('ip.in'): sys.stdin = open('ip.in', 'r'); sys.stdout = open('op.out', 'w')

def detri():
	n = int(input())
	arr = list(map(int, input().split()))
	ans = float("inf")
	total = sum(arr)
	for i in range(1<<n):
		s = 0
		for j in range(n):
			if i & 1<<j: s += arr[j]
		curr = abs((total-s)-s)
		ans = min(ans, curr)
	print(ans)

if __name__ == "__main__":
	detri()