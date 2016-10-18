__author__='Akash'
class  Person:
    TITLES=('mr','mrs','dr','miss')

    def __init__(self,name,surname):
        self.name=name  #instance attribute OR cached variables
        self.surname=surname  #instance attribute

    def fullname(self): #instance method
    #instance object accessible through self only
        return '%s %s' % (self.name, self.surname)

    @classmethod
    def allowed_titles_starting_with(self, startswith): #class method
        #class or instance object accessible through self/cls
        return [t for t in self.TITLES if t.startswith(startswith)]
    
    @staticmethod
    def allowed_titles_ending_with(endswith): #static method
        # no parameter for class or instance object
        #we have to use Person directly
        return [t for t in Person.TITLES if t.endswith(endswith)]

def main():
    jae = Person('Friday', 'Veronica')

    print(jae.fullname())
    # print(Person.fullname())  // this gives error bcz instance method cant called using class name
    print(jae.allowed_titles_starting_with('m'))
    print(Person.allowed_titles_starting_with('m'))

    print(jae.allowed_titles_ending_with('r'))
    print(Person.allowed_titles_ending_with('r'))


if __name__=='__main__':
    main()