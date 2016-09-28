__author__='Akash'
def function():
	a=input('Enter the no: ')
	fact=1
	while a>0:
		fact=fact*a
		a-=1
	print 'Factorial: ', fact
if __name__=='__main__':
	function()
