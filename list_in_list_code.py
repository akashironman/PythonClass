__author__='Akash'

def function():
	a=[['abc',37.21],['PQR',38],['xyz',37.2]]
	print a
	a.sort()
	for ele in a:
		tmp=ele[0]
		tmp1=ele[1]
		print tmp,tmp1,'%'

if __name__=='__main__':
	function()
