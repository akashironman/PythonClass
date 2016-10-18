__author__='Akash'

class Contact:

	all_name = []
	
	def __init__(self, name):
		self.name = name
		self.all_name.append(name)
		#print('List append in Contact class (Super): ', name)

	def print_Contact(self, *args):
		print 'In print ', Contact.all_name

class Friend(Contact):
	def __init__(self, name, phone):
		# self.all_name.append(name)
		#Contact.all_name.append(name)
		Contact.__init__(self, name)
		#print('List append in Friend class (Child): ', name)
		self.phone = phone

def Func():
	f=Friend('Mini', '1233')
	f=Friend('Akash', '4567')

	c=Contact('Patil')
	if isinstance(f, Friend):
		print f
	print c.all_name
	#c.print_Contact()

if __name__ == '__main__':
	Func()