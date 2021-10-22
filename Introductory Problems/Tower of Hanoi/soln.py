import sys,os.path

if os.path.exists('ip.in'): sys.stdin = open('ip.in', 'r'); sys.stdout = open('op.out', 'w')
	
moves = []

def towerOfHanoi(disks, start=1, end=3):
	if disks:
		towerOfHanoi(disks-1, start, 6-start-end)
		moves.append((start, end))
		towerOfHanoi(disks-1, 6-start-end, end)

def detri():
	towerOfHanoi(int(input()))
	print(len(moves))
	for m1, m2 in moves:
		print(m1, m2)

if __name__ == "__main__":
	detri()