T=input()
for f in range(T):
	s,n = raw_input().split()
	n=int(n)
	t=n
	q=len(s)-1
	if(n>0):
		while(t>0):
			s=s[q]+s[0:q]
			t=t-1
	else:
		while(t<0):
			s=s[1:q+1]+s[0]
			t=t+1

	print(s)
