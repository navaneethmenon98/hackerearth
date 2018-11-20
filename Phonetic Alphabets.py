a=['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey','Xray','Yankee','Zulu','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Zero']

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']


T=input()
for f in range(T):
	c=''
	d=''
	typ=raw_input()
	S=raw_input().split()
	if(typ=='phonetic'):
		for x in range(len(S)):
			if(S[x] in a):
				i=a.index(S[x])
				c=c+alpha[i]
		print(c.capitalize())
	if(typ=='english'):
		S[0]=S[0].lower()
		q=S[0]
		for y in range(len(q)):
			if(q[y] in alpha):
				i=alpha.index(q[y])
				d=d+a[i]+' '
		print(d)

