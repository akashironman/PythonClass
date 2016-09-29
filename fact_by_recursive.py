__author__='Akash'
def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

def fact():
	n=input('Enter number to find factorial: ')
	fact = factorial(n)
	print 'Factorial', fact

if __name__=='__main__':
	fact()
