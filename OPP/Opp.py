
from os import name


class studentAge():
    x = 30
    def __init__(self):
       
        i f(self.x = =20):
            print('This x values is 20')

    def updatePrint(self, param):
        pass


def update( self, m):
        print(m ,'this values is ', m)

        self.x = m ** self.x
        print(self.x, 'This man is self.x')

        for i in range(self.x):
            if (i ==399):
                break 
            print( 'This values is i')
           

    def updatePrint(self, m):
        print('This values is m' ,m)
        return self.update(m)             
    





a = studentAge()




a.updatePrint(3)


class Opp(object):
    def __init__(self , Name):
        print( 'self.name is values :' ,Name)


class In(Opp):

    def __init__(self):
        super().__init__('In')


a = In()


class Animal(object):
    def __init__(self, animal_type, x):
        print('Animal Type:', animal_type, x)
        print('hello world')


class Mammal(Animal):
    def __init__(self):
        super().__init__('Mammal', 'x')
        print('Mammals give birth directly')


dog = Mammal()

Name = 'Azimul Islam'

roll = 90

print(f'Name is{Name} with roll {roll}')

x = 20
y = 60
z = 'as is values z'

m = 'x is a first variable: %s. y is a second variable: %s values z :%s' % (str(x), str(y), z)

print(m)


class Dog_:
    species = "Cains familiars"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.species = 'Update Cains Familiars'

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


x = Dog_('Masan', 80)

var = x.species


class opp(object):
    def __init__(self, name):
        print('Name : -', name)

        for i in name:
            print(i, 'This values is i')


class sup(opp):

    def __init__(self):
        print('super class call')
        super().__init__('Romjan')
        super().__init__('Sotter')
        super().__init__('Robin')


x = opp('Kiddos')

y = sup()

y


class Rectangle:
    def __init__(self, length, width, hight):
        self.length = length
        self.width = width
        self.hight = hight
        print(self.length, 'length')
        print(width, 'width')
        print(hight, 'higth')

    def area(self):
        print(self.length * self.width * self.hight)
        return self.length * self.width * self.hight

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        print(self, length)
        super().__init__(length, length, length)


a = Square()


class Root:
    def draw(self):
        # the delegation chain stops here

        #chake arror
        # assert not hasattr( super(),'draw')
        print('hello')


class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)

    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super().draw()


class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)

    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()


cs = ColoredShape(color='blue', shapename='square', )


# cs.draw()


class Address(object):
    def __init__(self, first_name, lastName):
        self.first_name = first_name
        self.lastName = lastName

    def fullName(self):
        print(self.first_name + self.lastName)


class UserAddress(Address):
    def __init__(self, first_name, lastName):
        super().__init__(first_name, lastName)


class UserAddressFinal(UserAddress):
    def __init__(self, first_name, lastName):
        super().__init__(first_name, lastName)


x = UserAddressFinal("Aimful", 'Islam')

x.fullName()


class Root:
    def draw(self):
        # the delegation chain stops here
        print('hello')


class Shape(Root):
    def __init__(self, safe_name, **kwds):
        self.safe_name = safe_name
        super().__init__(**kwds)

    def draw(self):
        print('Drawing.  Setting shape to:', self.safe_name)
        super().draw()


class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)

    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()


cs = ColoredShape(color='blue', safe_name='square')
# cs.draw()

cs.draw()

__maxprice = 20

x = "Selling Price: {}".format(__maxprice)
y = f'"Selling Price: {__maxprice}'

print(x)
print(x)
