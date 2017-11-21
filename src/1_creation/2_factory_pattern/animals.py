from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Dog say:Guau!!")


class Cat(Animal):
    def do_say(self):
        print("Cat say:Miau!!")


class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


## client code
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)
