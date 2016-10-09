__author__='Akash'
def func():
    pno=raw_input('Enter pan no.: ')
    pno=pno.upper()
    print 'pan no: ',pno
    if len(pno)>10:
        print 'Invalid no'
    
    if pno[0:5].isalpha():
        print 'alpha is valid'
    else:
        exit()
    
    if pno[3]!='P'and pno[3]!='F' and pno[3]!='C':
        print ' Invalid Pan no'
        exit()
    
    if pno[5:9].isdigit():
        print 'Numeric is valid'
    else:
        print 'Numeric is invalid'
        exit()
    
    if pno[9].isalpha():
        print 'Last aplpha is valid'
        print 'Pan Number is valid'
if __name__=='__main__':
    func()