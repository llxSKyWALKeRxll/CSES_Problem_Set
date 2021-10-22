# import sys
# sys.stdin = open("ip.in","r")
# sys.stdout = open("op.out","w")

def detri():
	n = int(input())
	arr = [i for i in range(1,n+1)]
	arr = arr[1::2]+arr[::2]
	for i in range(1,n):
		if abs(arr[i]-arr[i-1])==1: print("NO SOLUTION"); exit()
	print(*arr)

if __name__ == "__main__":
	detri()