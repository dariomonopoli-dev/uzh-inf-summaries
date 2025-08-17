

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, mileage, capacity):
        super().__init__(name, mileage, capacity)

    def fare(self):
       final_amount = super().fare() + 0.1*(super().fare())
       return final_amount


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
print(type(School_bus))
print(isinstance(School_bus, Vehicle))


class Triangle:
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        return False

my_triangle = Triangle(90,30,60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)

happy_bday = Songs(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])

happy_bday.sing_me_a_song()


class Lunch:
    def __init__(self, menu):
        self.menu = menu

    def menu_price(self):
        if self.menu == 'menu 1':
            print('Your choice:', self.menu, 'Price 13.40')
        else:
            print('Error in menu')

Paul = Lunch('menu 1')
Paul.menu_price()


class Address:
    def __init__(self, street, num):
        self.street_name = street
        self.number = num


class CampusAddress(Address):
    def __init__(self, office_number, street='Massachusetts Ave', num = 77):
        self.office_number = office_number
        super().__init__(street, num)

Sarina_addr = CampusAddress('32-G904')
print(Sarina_addr.office_number)
print(Sarina_addr.street_name)
print(Sarina_addr.number)