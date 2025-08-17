#inheritance final hs 18
from abc import ABC, abstractmethod
class FileSystemItem(ABC):
    
    @abstractmethod
    def size(self):
        pass

class File(FileSystemItem):
    def __init__(self,size):
        self.__size = size
    def size(self):
        return self.__size

class Folder(FileSystemItem):
    def __init__(self, children):
        self.__children = children

    def size(self):
        somma=0
        if self.__children == []:
            return 0 
        for i in self.__children:
            somma+=i.size()
        return somma
    


assert File(1).size() == 1
assert Folder([]).size() == 0
assert Folder([File(2), File(3)]).size() == 5
assert Folder([File(4), Folder([File(5)])]).size() == 9



class Classroom:
    def __init__(self):
        self.students = {}

    def add(self, s):
        if s.matno in self.students:
            raise ValueError
        self.students[s.matno] = s


    def remove(self, matno):
        if matno not in self.students:
            raise IndexError
        del self.students[matno]


class Student:
    matno = 0
    def __init__(self, fname, lname, matno=0):
        self.fname = fname
        self.lname = lname
        self.matno = Student.matno
        Student.matno+=1

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
s1 = Student("Alice", "Bauer")
s2 = Student("Jack", "Wonderland")
assert(s1.matno == 0)
assert(s2.matno == 1)
c = Classroom()
c.add(s1)
c.add(s2)
assert(len(c.students) == 2)
c.remove(s2.matno)
assert(len(c.students) == 1)
try: # adding a student already in c
    c.add(s1)
    assert(False) # expected a ValueError!
except ValueError:
    pass # the correct exception has been thrown
try: # removing a student not in c
    c.remove(s2.matno)
    assert(False) # expected a ValueError!
except IndexError:
    pass # the correct exception has been thrown



import random

class Person:
    def __init__(self, name=None, sex=None):
        if name is None:
            self.name = name
        if sex is None:
            sex=random.choice(['m','f'])
        self.name = name
        self.sex = sex
        self.offspring = []


    def mate_with(self, person):
        if self.sex == person.sex:
            raise ValueError
        myperson = Person()
        self.offspring.append(myperson)
        person.offspring.append(myperson)
        return myperson

    def __str__(self):
        name_self_offspring = [i.name for i in self.offspring]
        string_name_offspring = ', '.join(name_self_offspring)
        if self.offspring==[]:
            return f'{self.name} ({self.sex}) has no children'
        if len(self.offspring)==1:
            return f'{self.name} ({self.sex}) has 1 child: {string_name_offspring}'
        return f'{self.name} ({self.sex}) has {len(self.offspring)} children: {string_name_offspring}'

    def __repr__(self):
        return self.__str__()
    

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
p1 = Person("Mark", "m")
p2 = Person("Betty", "f")
p3 = Person("John", "m")
p4 = Person("Anna", "f")
child = p1.mate_with(p2)
assert(child.name == None)
child.name = "Andrea"
assert(len(p1.offspring) == 1)
child = p3.mate_with(p2)
assert(len(p2.offspring) == 2)
child.name = "Terry"
assert(p1.__str__() == "Mark (m) has 1 child: Andrea")
assert(p2.__str__() == "Betty (f) has 2 children: Andrea, Terry")
assert(p3.__repr__() == "John (m) has 1 child: Terry")
assert(p4.__repr__() == "Anna (f) has no children")
try:
    p1.mate_with(p3)
    assert(False) # expected a ValueError!
except ValueError:
    pass # the correct exception has been thrown


from abc import ABC, abstractmethod
import unittest

class Product(ABC):

    @abstractmethod
    def get_price(self):
        pass

class Bottle(Product):
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def get_price(self):
        return self.price 

class Crate(Product):
    def __init__(self):
        self.__quantity = []

    def add(self, item):
        if len(self.__quantity)>=20:
            raise RuntimeError
        self.__quantity.append(item)

    def get_price(self):
        summe = 0
        for element in self.__quantity:
            summe +=element.get_price()
        return summe
            
    def get_size(self):
        return len(self.__quantity)


class DiscountCrate(Crate):
    def get_price(self):
        price = super().get_price()
        number_of_bottles = self.get_size()
        discount = 2* number_of_bottles
        if discount > 25:
            discount = 25
        price-= (discount/100)*price
        return round(price, 2)


class FixedPriceCrate(Crate):
    def __init__(self, price):
        super().__init__()
        self.price = price

    def get_price(self):
        return self.price

class ShopTestSuite(unittest.TestCase):

    def test_crate_add(self):
        c = Crate()
        c.add(Bottle(4.50, "Light Beer"))
        self.assertEqual(c.get_size(), 1)

    def test_crate_max_size(self):
        c=Crate()
        bottle = [Bottle(3.50, "Light Beer")]
        with self.assertRaises(RuntimeError):
            for i in range(21):
                c.add(bottle)

    def test_crate_price(self):
        c = Crate()
        bottles = [Bottle(5.00, "Light Beer"), Bottle(5.00, "Passable Wine")] + 3 * [Bottle(5.00, "Strong Stuff")]
        for b in bottles:
            c.add(b)
        actual = c.get_price()
        expected = 25
        self.assertEqual(actual, expected)

    def test_discount_crate_price(self):
        d = DiscountCrate()
        bottles = [Bottle(5.00, "Light Beer"), Bottle(5.00, "Passable Wine")] + 3 * [Bottle(5.00, "Strong Stuff")]
        for b in bottles:
            d.add(b)
        self.assertEqual(d.get_price(), 22.5)

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
bottles = [Bottle(3.50, "Light Beer"), Bottle(4.50, "Passable Wine")] + 3 * [Bottle(4.00, "Strong Stuff")]
assert(bottles[0].get_price() == 3.50)

c = Crate()
for b in bottles: c.add(b)
assert(c.get_size() == 5)
assert(c.get_price() == 20.00)

c = FixedPriceCrate(11.11)
for b in bottles: c.add(b)
assert(c.get_price() == 11.11)

c = DiscountCrate()
for b in bottles: c.add(b)
assert(c.get_price() == 18.00)

unittest.main()
    