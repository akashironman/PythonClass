"""List exercize 21/oct/2016"""

__author__='Akash'

def main():
    str_list=['xyz', 'abc', 'aba', 'lzzl', 'aa']
    print str_list
    print 'string having length more than 2 & first and last character same are'
    count=0
    for ele in str_list:
        if len(ele)>2 and ele[0]==ele[-1]:
            count+=1
    
    print 'count of elements are: ', count
if __name__=='__main__':
    main()