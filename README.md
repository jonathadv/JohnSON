# JohnSON
A simple Object-to-JSON serializer class


**Usage:**
```python
from JohnSON import JSONable

"""
Your class should inherit from JSONable to have the ``to_json()`` method.

Optionally you can add the ``to_json()`` call in ``__str__()``.
"""
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

```
***print(a) output***
```json
{"age": 12, "name": "Ted", "friend": null}
```
***print(b) output***
```json
{"age": 24, "name": "Roy", "friend": {"age": 12, "name": "Ted", "friend": null}}
```

***print(c) output***
```json
{
    "age": 82,
    "name": "Junior",
    "friend": [
        {
            "age": 12,
            "name": "Ted",
            "friend": null
        },
        {
            "age": 24,
            "name": "Roy",
            "friend": {
                "age": 12,
                "name": "Ted",
                "friend": null
            }
        }
    ]
}
```
