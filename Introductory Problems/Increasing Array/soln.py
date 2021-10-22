# import sys
# sys.stdin = open("ip.in","r")
# sys.stdout = open("op.out","w")

def detri():
	n = int(input())
	arr = list(map(int, input().split()))
	ans = 0
	for i in range(1, n):
		if arr[i]<arr[i-1]:
			req = arr[i-1]-arr[i]
			ans += req
			arr[i] += req
	print(ans)

if __name__ == "__main__":
	detri()