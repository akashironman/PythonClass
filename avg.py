__author__='Akash'
def func():
    students=[{'name':'xyz','marks':50},{'name':'pqr','marks':50}, {'name':'abc','marks':50}]
    a=0
    # for stud in students:
    print students 
    for stud in students:
        a=a+stud['marks'] 
    print a/len(students)
if __name__=='__main__':
    func()