__author__='Akash'
def divide(x,y):
    try:
        result=x/y
    except Exception as e:
        print 'Exeption is: ', e
    else:
        print 'Result is: ', result
    finally:
        print 'executing finally block'
if __name__=='__main__':
    a=input('Enter 1st no.: ')
    b=input('Enter 2nd no.: ')
    divide(a,b)