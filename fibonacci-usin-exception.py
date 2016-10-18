__author__='Akash'
def func():
	f=1
	while f==1:
		try:
			temp=int(raw_input('Enter the count to print febonaci series : '))
			if temp<=0:
				print 'count invalid '
			else:
				f=0
		except Exception as e:
			print e

	a,b=0,1
	s=[a]
	while temp>1:
		a,b=b,a+b
		s.append(a)
		temp-=1
	print s	
	print 'cubes of fibo:'
	for i in xrange(len(s)):	
		s[i]=s[i]**3
	print s	
if __name__=='__main__':
	func()
