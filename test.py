# print(3*3)
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


num1 = ComplexNumber(2, 3)
num1.get_data()


num2 = ComplexNumber(5)
num2.attr = 10

print((num2.real, num2.imag, num2.attr))
print(num1.attr)


class Cylinder:
    pi = 3.14

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return Cylinder.pi * self.radius ** 2 * self.height

    @classmethod
    def description(cls):
        return f'EEEESKETTTiiTTTT={cls.pi}'


if __name__ == '__main__':
    c1 = Cylinder(4, 2)

    print(f'Volume of Cylinder: {c1.volume()}')
    print(Cylinder.description())
    print(c1.description())