T=input()
a=['a','e','i','o','u','A','E','I','O','U']
for f in range(T):
	d=''
	S=map(str,raw_input().split())
	for i in range(len(S)):
		b=S[i]
		if b[0] in a:
			b=b+'ay'
		else:
			c=len(b)
			b=b[1:c]+b[0]+'ay'
		S[i]=b
		for t in range(len(b)):
			d=d+b[t]
		d=d+' '
	print(d)
			
	
