class Animal:
    def __init__(self,age, breed):
        self.age = age
        self.breed = breed
class Cat(Animal):
    def torna_value(self):
        return self.age


class Dog(Animal):
    def __init__(self, name,age, breed):
        self. age = age
        self.breed = breed
        self.name= name
    def torn_value(self):
        return self.age
    def __str__(self):
        return f'{self.name} is a {self.breed} and is {self.age} years old'


c2=Dog('fido',3,'chiuaua')
print(c2)
print(c2.age)

#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

class Serializer(ABC):
    def serialize(self, person):
        template = self.lineTemplate()
        return template % (self.formatName(person.name),
                           self.formatAge(person.age),
                           self.formatHeight(person.height))

    @abstractmethod
    def lineTemplate(self):
        pass

    @abstractmethod
    def formatName(self, name):
        pass

    @abstractmethod
    def formatAge(self, age):
        pass

    @abstractmethod
    def formatHeight(self, height):
        pass

class SentenceSerializer(Serializer):
    def lineTemplate(self):
        return "%s is %s old and %s tall"

    def formatName(self, name):
        return name

    def formatAge(self, age):
        if age == 1:
            return f"{age} year"
        return f"{age} years"

    def formatHeight(self, height):
        return f"{height}cm"

class CSVSerializer(Serializer):
    def lineTemplate(self):
        return "%s,%s,%s"

    def formatName(self, name):
        return f'"{name}"'

    def formatAge(self, age):
        return age

    def formatHeight(self, height):
        return height

class HTMLSerializer(Serializer):
    def lineTemplate(self):
        return "<li>%s (%s): %s</li>"

    def formatName(self, name):
        return name

    def formatAge(self, age):
        return age

    def formatHeight(self, height):
        return f"{height / 100}m"

p = Person("Ann", 31, 168)
s1 = SentenceSerializer()
print(s1.serialize(p))
s2 = CSVSerializer()
print(s2.serialize(p))
s3 = HTMLSerializer()
print(s3.serialize(p))

class HtmlBlockSerializer:
    def serializeBlock(self, serializer, persons):
        res = "<ul>\n"
        for p in persons:
            res += serializer.serialize(p) + "\n"
        res += "</ul>"
        return res

bs = HtmlBlockSerializer()
print(bs.serializeBlock(s3, [p, Person("Bob", 28, 191)]))

#inheritance/vererbung
print('la classe è il bauplan, le instance sono gli oggetti che condividono le caratteristiche del bauplan ma sono diverse tra i diversi oggetti')
