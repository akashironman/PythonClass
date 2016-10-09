__author__='Akash'
def func():
    a=[5,3,4,1,2,13,12,13]
    print a
#    print len(a)
    for i in xrange(len(a)-1):
        for j in xrange(len(a)-i-1):
            if a[j]<a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    print a
if __name__=='__main__':
    func()