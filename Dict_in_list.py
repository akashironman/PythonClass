__author__='Akash'
def func():
    students=[{'name':'xyz','marks':50},{'name':'pqr','marks':50}, {'name':'abc','marks':50}]
    print students
    a={'name':'Akash','marks':75}
    students.extend(a)
    print 'after extend: ', students
    students.append(a)
    print 'after append: ', students
if __name__=='__main__':
    func()