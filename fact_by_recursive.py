__author__='Akash'
def fact():
	n=input('Enter number to find factorial: ')
	def factorial(n):
		if n==0:
			return 1
		else:
			return n*factorial(n-1)
	print 'Factorial', fact
if __name__=='__main__':
	fact()
