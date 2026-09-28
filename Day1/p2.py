class product:
    def __init__(self,pID,pNAME):
        '''product initialization'''
        self.pid = pID
        self.pname = pNAME
        print(f'Product {self.pname} initialization')
    def display(self):
        print(f'About {self.pname} product details:-')
        print(f'product name:{self.pname} pid:{self.pid}')

'''
obj1 = product()
obj1.initialization(101,'pA')

obj2 = product()
obj2.initialization(102,'pB')
print('\n')
obj1.display()
obj2.display()
'''
obj1 = product(101,'pA')
obj1.display()