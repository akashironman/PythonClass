'''updating dictionary with elements other dictiory elements'''
__author__='Akash'

def main():
    dict_1={1:100, 2:200}
    dict_2={3:300, 4:400}
    dict_3={5:500, 6:600}
    print 'three dict are: '
    print dict_1,' ', dict_2,' ', dict_3
    print 'updating these elements of dict to new dict_4'
    dict_4=dict()
    for ele in (dict_1, dict_2, dict_3):
        dict_4.update(ele)
    print dict_4
if __name__=='__main__':
    main()