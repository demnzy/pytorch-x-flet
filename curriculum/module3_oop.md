# Day 1 - Module 3: Object-Oriented Programming (OOP) (40 mins)

This is a crucial concept. Everything in PyTorch and Flet (our Machine Learning and UI tools) relies on Object-Oriented Programming (OOP).

## 1. Classes vs. Objects (10 mins)

Think of a **Class** as a **blueprint** for a house. The blueprint itself isn't a house—you can't live in it. But it tells the builders exactly how to make the house, what color it should be, and how many doors it has.

An **Object** is the actual physical house built from that blueprint. You can build 10 houses (Objects) from 1 blueprint (Class).

In Python, we can create our own blueprints using the `class` keyword.

## 2. The Magic `__init__` Method and `self` (15 mins)

When you tell Python to build an object from your blueprint, it automatically looks for a special function inside the class called `__init__` (short for initialize). This is the "constructor"—the team of builders that sets up the house.

Inside a class, functions are called **Methods**. Every method inside a class must have a special first parameter called `self`. `self` refers to the specific object being built.

```python
# The Blueprint
class Dog:
    # The builders that set up the dog when it is born
    def __init__(self, dog_name):
        # We attach the name to *this specific dog* (self)
        self.name = dog_name  

    # A behavior the dog can do
    def bark(self):
        print(self.name + " says Woof!")

# The Objects
dog1 = Dog("Buddy") # This automatically runs __init__, setting self.name to "Buddy"
dog2 = Dog("Max")   # This sets self.name to "Max" for the second dog

dog1.bark() # Prints: Buddy says Woof!
dog2.bark() # Prints: Max says Woof!
```
Notice how `dog1` and `dog2` are built from the exact same blueprint, but they contain different data!

## 3. Inheritance and `super().__init__()` (15 mins)

Sometimes you want to build a blueprint based on an *existing* blueprint. For example, a `Poodle` is a specific type of `Dog`. It shares all the traits of a `Dog` (like having a name and barking), but might have extra traits.

This is called **Inheritance**. We put the parent class in parentheses: `class Poodle(Dog):`

When a Poodle is built, we want to make sure the original `Dog` builders run first (to give it a name), before the `Poodle` builders do their extra work. We do this by calling `super().__init__()`. The word `super()` refers to the "parent" blueprint.

```python
class Poodle(Dog): # Poodle inherits from Dog
    def __init__(self, dog_name):
        # Call the parent's (Dog's) __init__ to handle the name
        super().__init__(dog_name)
        
        # Now do the specific Poodle setup
        self.haircut = "Fancy"
```

**Why does this matter?**
When we build our Machine Learning AI later, we will write:
`class AirQualityModel(nn.Module):`
This means our model will inherit all the magical mathematical capabilities of PyTorch's built-in `nn.Module` blueprint, and we will use `super().__init__()` to make sure PyTorch sets up the complex math engines before we add our specific layers to it!
