"""List exercize 2 21/oct/2016"""
'''print only 1st and third element form list'''
__author__='Akash'

def main():
    str_list=['xyz', 'abc', 'aba', 'lzzl', 'aa']
    print str_list
    print 'printing only first and third element'
    a=[]
    # ab=[x for (i,x) in enumerate(str_list) if i not in (2,4,0)]
    for st in xrange(len(str_list)):
        if st%2==1: #my logic
            #print str_list[st]
            a.append(str_list[st])
    print a
if __name__=='__main__':
    main()