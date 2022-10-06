# Try forcing the not implemented error to check whether the try catch is where it should be!!!

class Zoo:
    def __init__(self, name=None):
        self._name = name
        self._zoo_animals = []

    def add_animal(self, animal):
        self._zoo_animals.append(animal)

    def test_animals(self):
        print('zoo name:', self._name)
        print('number of animals:', len(self._zoo_animals))
        for animal in self._zoo_animals:
            print('name:', animal.get_name())
            animal.sleep()
            animal.make_noise()
            while animal.get_hunger_level() > 0:
                animal.eat()
            print('hunger_level:', animal.get_hunger_level())
            animal.roam()
            if isinstance(animal, Pet):
                animal.play()
                animal.be_friendly()

            print('-------------------')


class Animal:
    def __init__(self, name=None):
        self._name = name
        self._hunger_level = 0

    def get_hunger_level(self):
        return self._hunger_level

    def set_hunger_level(self, value):
        self._hunger_level = 0 if value < 0 else 10 if value > 10 else value

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def sleep(self):
        print('sleeping...')
        self.set_hunger_level(10)

    def roam(self):
        self.set_hunger_level(self.get_hunger_level() + 1)
        print('moving around...')

    def make_noise(self):
        raise NotImplementedError

    def eat(self):
        raise NotImplementedError


class Pet:
    def play(self):
        raise NotImplementedError

    def be_friendly(self):
        raise NotImplementedError


class Feline(Animal):
    def roam(self):
        self.set_hunger_level(self.get_hunger_level() + 1)
        print('felines like to roam alone...')


class Canine(Animal):
    def roam(self):
        self.set_hunger_level(self.get_hunger_level() + 1)
        print('canines like to roam in packs...')


class Hippo(Animal):
    def make_noise(self):
        print('blub...')

    def eat(self):
        self.set_hunger_level(self.get_hunger_level() - 1)
        print('slurp...')


class Lion(Feline):
    def make_noise(self):
        print('roar...')

    def eat(self):
        self.set_hunger_level(self.get_hunger_level() - 2)
        print('rip with teeth...')


class Cat(Pet, Feline):
    def make_noise(self):
        print('meow...')

    def eat(self):
        self.set_hunger_level(self.get_hunger_level() - 3)
        print('pick...')

    def play(self):
        print('frolic...')

    def be_friendly(self):
        print('purr...')


class Wolf(Canine):
    def make_noise(self):
        print('growl...')

    def eat(self):
        self.set_hunger_level(self.get_hunger_level() - 2)
        print('rip with teeth...')


class Dog(Canine, Pet):
    def make_noise(self):
        print('bark...')

    def eat(self):
        self.set_hunger_level(self.get_hunger_level() - 3)
        print('slop...')

    def play(self):
        print('scamper...')

    def be_friendly(self):
        print('sniff...')


def main():
    dog = Dog('Red')
    cat = Cat('Millie')
    lion = Lion('Aslan')
    wolf = Wolf('River')
    hippo = Hippo('Henrietta')
    zoo = Zoo("Withnail's")
    zoo.add_animal(dog)
    zoo.add_animal(wolf)
    zoo.add_animal(cat)
    zoo.add_animal(hippo)
    zoo.add_animal(lion)
    zoo.test_animals()


if __name__ == '__main__':
    main()
