__author__='Akash'

def Function():
	print '----------------------------------------------'
	print 'Program for [](){} type checking:'
	print '----------------------------------------------'
	string=raw_input('Enter the parenthesis string: ')
	flag =1
	if len(string)%2==1:
		flag=0
	for i in xrange(0,len(string)-1,2):
		# print i
		if (string[i]=='(' and string[i+1]==')') or (string[i]=='[' and string[i+1]==']') or (string[i]=='{' and string[i+1]=='}'):
			pass
		else:
			flag=0
	if flag==0:
		print 'invalid string'
	else:
		print 'valid string'	

if __name__=='__main__':
	Function()
