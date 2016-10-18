__author__='Akash'
def func():
	temp=input('Enter the count to print fibonacci series : ')
	a,b=0,1
	s=[]
	while temp>=1:
		s.append(a)
		a,b=b,a+b
		temp-=1
	print s
if __name__=='__main__':
	func()
