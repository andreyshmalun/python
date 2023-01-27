# class Date(object):
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def get_date(self):
#         output = str(self.day) + '/' + str(self.month) + '/' + str(self.year)
#         return output

#     def set_date(self):
#         self.day = int(input('Enter the day: '))
#         self.month = int(input('Enter the month: '))
#         self.year = int(input('Enter the year: '))

#     def is_leap_year(self):
#         return self.year % 4 == 0

#     def is_valid_date(self):
#         if not (type(self.day) == int and type(self.month) == int and type(self.year) == int):
#             return False
#         if self.year < 0:
#             return False
#         if self.month < 1 or self.month > 12:
#             return False

#         last_dates = {
#             1: 31,
#             2: 29 if self.is_leap_year() else 28,
#             3: 31,
#             4: 30,
#             5: 31,
#             6: 30,
#             7: 31,
#             8: 31,
#             9: 30,
#             10: 31,
#             11: 30,
#             12: 31
#         }

#         if self.day < 1 or self.day > last_dates.get(self.month):
#             return False
#         return True


# date1 = Date(29, 2, 2000)
# date2 = Date(29, 2, 2001)
# date3 = Date('abc', 'def', 'ghi')

# print(str(date1.get_date()) + ': ' + str(date1.is_valid_date()))
# print(str(date2.get_date()) + ": " + str(date2.is_valid_date()))
# print(str(date3.get_date()) + ": " + str(date3.is_valid_date()))

# class Cow(object):
#     def speak(self):
#         print('Moo!')


# class Dog(object):
#     def speak(self):
#         print('Woof!')


# cow = Cow()
# dog = Dog()


# class Date(object):
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def get_date(self):
#         output = str(self.day) + '/' + str(self.month) + '/' + str(self.year)
#         return output


# date = Date(1, 1, 2000)


# class ShoppingList:
#     def __init__(self, list_name):
#         self.list_name = list_name
#         self.shopping_list = []

#     def add_item(self, item):
#         if not item in self.shopping_list:
#             self.shopping_list.append(item)

#     def remove_item(self, item):
#         try:
#             self.shopping_list.remove(item)
#         except:
#             print('Item not found')

#     def view_list(self):
#         print('\nItems in ' + str(self.list_name) + '\n' + 30*'-')
#         for item in self.shopping_list:
#             print(' - ' + str(item))

#     def merge_lists(self, obj):
#         merged_lists_name = 'Merged list - ' + \
#             str(self.list_name) + ' + ' + str(obj.list_name)
#         merged_lists_obj = ShoppingList(merged_lists_name)
#         merged_lists_obj.shopping_list = self.shopping_list.copy()
#         for item in obj.shopping_list:
#             if not item in merged_lists_obj.shopping_list:
#                 merged_lists_obj.shopping_list.append(item)

#         return merged_lists_obj


# pet_store_list = ShoppingList('Pet Store Shopping List')
# grocery_store_list = ShoppingList('Grocery Store List')

# for item in ['dog food', 'frisbee', 'bowl', 'collars', 'flea collars']:
#     pet_store_list.add_item(item)

# for item in ['fruits', 'vegetables', 'bowl', 'ice cream']:
#     grocery_store_list.add_item(item)

# merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)

# merged_list.view_list()
class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + ' feet, ' + str(self.inches) + ' inches'
        return output

    def __add__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        total_height = height_A_inches + height_B_inches
        output_feet = total_height // 12
        output_inches = total_height - (output_feet * 12)
        return Height(output_feet, output_inches)

    def __sub__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        total_height = height_A_inches - height_B_inches
        output_feet = total_height // 12
        output_inches = total_height - (output_feet * 12)
        return Height(output_feet, output_inches)

    def __lt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A < height_inches_B

    def __le__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A <= height_inches_B

    def __eq__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A == height_inches_B

    def __gt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A > height_inches_B

    def __ge__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A >= height_inches_B

    def __ne__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A != height_inches_B


height_1 = Height(4, 10)
height_2 = Height(5, 6)
height_3 = Height(7, 1)
height_4 = Height(5, 5)
height_5 = Height(6, 7)
height_6 = Height(5, 6)


class Person:
    def walk():
        print('Hello, I can walk!')


class Athlete(Person):
    def run():
        print('Hey, I can run too!')


# Person.walk()
# Athlete.walk()
# Athlete.run()


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def __str__(self):
        output = "\nClass: Animal\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output


# a = Animal(5)
# print(a)


class Cat(Animal):
    def speak(self):
        print('Meow')

    def __str__(self):
        output = "\nClass: Cat\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output


class Dog(Animal):
    def speak(self):
        print('Woof!')

    def __str__(self):
        output = "\nClass: Dog\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output


# cat = Cat(3)
# dog = Dog(6)

# cat.set_name('Musya')
# dog.set_name('Sammy')

# print(cat)
# print(dog)

# cat.speak()
# dog.speak()


class Human(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    def show_friends(self):
        for friend in self.friends:
            print(friend)

    def speak(self):
        print("Hello, my name's " + self.name + "!")

    def __str__(self):
        output = "\nClass: Human\nName: " + str(self.name) + \
            "\nAge: " + str(self.age) + "\nFriends list: \n"
        for friend in self.friends:
            output += friend + "\n"
        return output


human = Human('Andrew', 33)
human.add_friend("Robert")
human.add_friend("Élise")
human.add_friend("Abdullah")
human.add_friend("Asha")
human.add_friend("Lupita")
human.add_friend("Saito")
# human.speak()
# print(human)


class Example(object):
    common_string = 'Hello, I can be accessed from anywhere!'

    def __init__(self, a, b):
        self.a = a
        self.b = b


alpha = Example(1, 2)
beta = Example(3, 4)

# alpha.common_string
# beta.common_string
# print(Example.common_string)
# Example.common_string = "I've changed!"
# print(Example.common_string)
# print(alpha.common_string)


class Car(object):
    id = 0

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.id = Car.id
        Car.id += 1

    def __str__(self):
        output = '\nID: ' + str(self.id) + \
            "\nName: " + self.name + \
            "\nModel: " + self.model + \
            "\nYear: " + self.year
        return output


c0 = Car("Ford", "Shelby GT500", "2015")
c1 = Car("Toyota", "Corolla", "2012")
c2 = Car("BMW", "Z3", "2001")
c3 = Car("Audi", "A6", "2020")

print(c0, c1, c2, c3)
