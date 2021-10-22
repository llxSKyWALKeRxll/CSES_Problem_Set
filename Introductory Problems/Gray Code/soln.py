import sys,os.path
if os.path.exists('ip.in'):
    sys.stdin = open('ip.in', 'r')
    sys.stdout = open('op.out', 'w')

from collections import *

def grayCode(n):
	if n<=0: return ["0"]
	if n==1: return ["0","1"]
	recCall = grayCode(n-1)
	ans = []
	for digit in recCall:
		ans.append("0"+digit)
	for digit in reversed(recCall):
		ans.append("1"+digit)
	return ans
	
def detri():
	n = int(input())
	for i in range(1<<n):
		val = i^(i>>1)
		val = bin(val).replace("0b", "")
		print(val if len(val)==n else "0"*(n-len(val))+val)

if __name__ == "__main__":
	# print(*grayCode(int(input())), sep="\n")
	detri()