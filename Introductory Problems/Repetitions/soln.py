# import sys
# sys.stdin = open("ip.in","r")
# sys.stdout = open("op.out","w")

s = input()
ctr=ans=1
for i in range(1, len(s)):
	if s[i]==s[i-1]: ctr += 1
	else: ctr = 1
	ans = max(ans,ctr)
print(ans)