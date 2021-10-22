import sys,os.path
if os.path.exists('ip.in'):
    sys.stdin = open('ip.in', 'r')
    sys.stdout = open('op.out', 'w')

from collections import *

def detri():
	s = input()
	if len(set(s))==1: print(s); exit()
	dictMap = dict(Counter(s))
	oddSeq = 0
	for key in dictMap:
		if dictMap[key]&1: oddSeq += 1; oddChar = key
	if oddSeq>1 or oddSeq==1 and not len(s)&1: print("NO SOLUTION"); exit()
	first, second = "", ""
	for char in sorted(dictMap.keys()):
		cut = (dictMap[char]//2)*char
		first += cut
		second = cut + second
	print(first+oddChar+second if oddSeq == 1 else first+second)

if __name__ == "__main__":
	detri()