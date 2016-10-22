'''Dictionary Exercize: adding elements'''

__author__='Akash'

def main():
    n=input('Enter count to print dict: ')
    d=dict()
    for i in xrange(1,n+1):
        d.update({i:i**2})
    print d
if __name__=='__main__':
    main()