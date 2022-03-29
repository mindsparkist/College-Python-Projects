# def add_sub(num_1, num_2):
#     add = int(num_1) + int(num_2)
#     sub = int(num_1) - int(num_2)
#     return add, sub


# num_1 = input("Enter a number: ")
# num_2 = input("Enter another number: ")

# add, sub = add_sub(num_1, num_2)
# print("Addition: ", add)
# print("Subtraction: ", sub)


# def person(name, age, **args):
#     print("Name: ", name)
#     print("Age: ", age)
#     for kw, arg in args.items():
#         print(kw, ":", arg)


# person("shuv", age=20, city="Mumbai", country="India")

# Classes In python

# class person:
#     def greet(self):
#         print("Hello")


# person1 = person()
# person.greet(person1)

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print("Hello" + " " + self.name + " " +
#               "Your Age Is" + " " + str(self.age) + " " + "Years")


# personobj = person("shuv", 20)
# person.greet(personobj)
