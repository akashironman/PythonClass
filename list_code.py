__author__='Akash'
def function():
	a_list=[]
	a_list.insert(0,1)
	print 'inserted 1 at 0 :',a_list
	a_list.insert(1,4)
	print 'inserted 4 at 1 :', a_list
	a_list.insert(1,5)
	print 'inserted 5 at 1: ', a_list
	a_list.remove(4)
	print 'removed 4: ', a_list
	a_list.append(9)
	print 'appended 9: ', a_list
	a_list.sort()
	print 'sorted list: ', a_list
	a_list.pop()
	print 'popped: ', a_list
	a_list.reverse()
	print 'reversed: ', a_list
if __name__=='__main__':
	function()
