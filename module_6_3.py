class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self):
        super().__init__()

    def __iadd__(self, value):
        return self.__iadd__(value)

    def run(self, dx):
        self.dx = dx
        Horse.x_distance += self.dx
        return Horse.x_distance


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __iadd__(self, value):
        return self.__iadd__(value)

    def fly(self, dy):
        self.dy = dy
        Eagle.y_distance += self.dy
        return Eagle.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        Horse.run(self, dx)
        Eagle.fly(self, dy)

    @staticmethod
    def get_pos():
        return Horse.x_distance, Eagle.y_distance

    @staticmethod
    def voice():
        print(Eagle.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
