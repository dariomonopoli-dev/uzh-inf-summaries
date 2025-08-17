import random

class Dog:
    def __init__(self, name,age,breed,sex):
        self.name=name
        self.age=age
        self.sex = sex
        self.breed = breed
        if sex not in ['male','female']:
            raise ValueError('invalid sex')
        self.sex = sex
        self.tricks = set() #sets are not ordered, and they do not return duplicates. Sets are mutable

    def learn_trick(self,new_trick):
        self.tricks.add(new_trick)
    
    def do_trick(self):
        if len(self.tricks)==0:
            raise Warning('do not know any tricks')
        return random.choice(self.tricks())


    def __str__(self):
        return f'Name: {self.name}, {self.breed},{self.age} years old'


    def __add__(self,other):
        if not self.sex !=other.sex:
            raise Warning('not possible!')
        import random
        new_sex = random.choice( ['male','female'])
        new_breed='Mutt'
        if self.breed == other.breed:
            new_breed=self.breed
        new = Dog(None,0,new_breed,new_sex)
        return new

d1=Dog('coco',3,'Collie','female')
d2=Dog('pepe',5,'Collie','male')
print(d1)
print(d2)
d3=d1+d2
print(d3)
d3.learn_trick('spin')
print(d3.do_trick())


