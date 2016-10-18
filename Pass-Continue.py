__author__='Akash'

def func():
	print('Demo of pass and continue:')

	for i in range(0,20):
		if  i%2 == 0: 
			pass
			print'In pass block i=', i 
		else:
			print('In else')
			continue
			print('In continue block ')
if __name__=='__main__':
	func()