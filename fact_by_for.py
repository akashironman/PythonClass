__author__='Akash'
def function():
	n=input('Enter no to find factorial: ')
	fact=1
	for i in range(n):
		i+=1
		fact=fact*i
	print 'Factorial: ',fact
if __name__=='__main__':
	function()
