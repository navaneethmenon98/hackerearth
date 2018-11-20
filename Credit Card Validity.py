T=input()
for f in range(T):
	N=input()
	s=0
	e=0
	oddcheck=0
	while(N>=1):
		b=N%10
		if(oddcheck%2==0):
			s=s+b
		else:
			c=b*2
			if(c>=10):
				while(c>=1):
					d=c%10
					e=e+d
					c=c/10
				s=s+e
				e=0
			else:
				s=s+c
		oddcheck=oddcheck+1
		N=N/10
	if(s%10==0):
		print('VALID')
	else:
		print('INVALID')
		
