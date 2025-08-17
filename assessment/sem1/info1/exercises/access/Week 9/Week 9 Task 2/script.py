#!/usr/bin/env python3

class Fridge():
    def __init__(self):
        self.__storage = []

    def __len__(self):
        return len(self.__storage)

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x < len(self.__storage):
            result = self.__storage[self.x]
            self.x +=1
            return result   # se non faccio return result non mi viene mai dato l'oggetto indietro
        raise StopIteration

    def store(self, tuple):
        self.__storage.append(tuple)
        self.__storage = sorted(self.__storage)
        return self.__storage

    def inventory(self):
        return self.__storage

    def find(self, name):
        for item in self.__storage:
            if item[1]==name:
                return item
            return None

    def take_before(self, date):
        expired_food = []
        for item in self.__storage:
            if date > item[0]:
                expired_food.append(item)
        for item in expired_food:
            if item in self.__storage:
                self.__storage.remove(item)
        return expired_food
            
    def take(self, item):
        if item not in self.__storage:
            raise Warning('Item not in Fridge!')
        self.__storage.remove(item)
        return item
        

if __name__ == '__main__':   
    f=Fridge()
    f.store((191127, 'Butter'))
    print(f.inventory())
    f.take((191127, 'Butter'))
    print(f.inventory())
    # f.take((12849, 'Cheese')


