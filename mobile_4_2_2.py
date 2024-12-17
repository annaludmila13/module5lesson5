class House:
    houses_history = []

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __repr__(self):
        return f'House({self.name}, {self.floors})'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        else:
            return NotImplemented

    def __iadd__(self, value):
        self.floors += value
        return self

    def __add__(self, value):
        new_floors = self.floors + value
        return House(self.name, new_floors)

    def __radd__(self, value):
        new_floors = self.floors + value
        return House(self.name, new_floors)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    @classmethod
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.houses_history.append(args[0])
        return instance
h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 30)

print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

