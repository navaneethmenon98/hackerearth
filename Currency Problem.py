T=input()
for f in range(T):
	N = int(raw_input())
	t=N
	s=0
	a=[1,2,5,10,20,50,100,200,500,2000]
	for i in range(len(a)):
		if(a[i]==t):
			s=1
	if(s==0):
		while(t>0):
			if(t>2000):
				r=2000
			else:
				for i in range(len(a)):
					if(a[i]>t):
						r=a[i-1]
						break
			s=s+1		
			t=t-r	
			r=0	
			
	print(s)
