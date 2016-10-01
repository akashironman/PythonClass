__author__='Akash'
def func():
	temp=input('Enter the count no. up to which you want to print febonaci series : ')
	a,b=0,1
	print a
	while temp>1:
		print a+b
		a,b=b,a+b
		temp-=1
if __name__=='__main__':
	func()
