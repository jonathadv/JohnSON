from johnson import JSONable

""" Test Class """
class Person(JSONable):
    def __init__(self, name, age, friend):
        self.name = name
        self.age = age
        self.friend = friend

    def __str__(self):
        return self.to_json()

a = Person('Ted', 12, None)
b = Person('Roy', 24, a)
c = Person('Junior', 82, [a,b])


print(a)
print(b)
print(c.to_json(pretty=True))
