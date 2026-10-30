# Day 1 - Module 2: Lists & Functions (30 mins)

In Module 1, we learned how to store single pieces of data in a variable. But what if we have a lot of data? Or what if we have a lot of instructions?

## 1. Python Lists (10 mins)
A **List** is a way to store multiple items in a single variable. Think of it like a shopping list. In Python, lists are created using square brackets `[]`, and items are separated by commas.

```python
# A list of integers
lucky_numbers = [7, 13, 42]

# A list of strings
weather_features = ["Temperature", "Humidity", "PM2.5"]
```
When we build our Machine Learning model later, we will use lists extensively to feed multiple numbers into the brain at the same time.

## 2. Functions & Parameters (20 mins)
Imagine you have a complex recipe to make coffee. Instead of writing down all 10 steps every single time you want coffee, you write them down once, label the paper "Make Coffee", and whenever you want coffee, you just point to the paper and say "Make Coffee."

In Python, this reusable block of code is called a **Function**. 

### Defining a Function (`def`)
To create a function, you use the `def` keyword (short for define). Everything indented under the `def` line belongs to that function.

```python
def make_coffee():
    print("Grinding beans...")
    print("Pouring water...")
    print("Coffee is ready!")
```
Notice that running the code above does *nothing*. We wrote the recipe, but we didn't tell the computer to actually *make* the coffee. 

### Calling a Function
To tell the computer to execute the recipe, you "call" it by writing its name followed by parentheses `()`.

```python
make_coffee() 
# Now the computer will print the 3 lines!
```

### Parameters (Giving the function ingredients)
Sometimes a recipe needs ingredients. You can pass variables into a function. These are called **Parameters**.

```python
def make_coffee(sugar_cubes):
    print("Brewing coffee...")
    print("Adding " + str(sugar_cubes) + " sugar cubes.")

make_coffee(2) # We pass the number 2 into the function
```

### The `return` Keyword (Getting something back)
Often, you want a function to do some math and give the answer back to you, rather than just printing it to the screen. You use the `return` keyword to hand the final result back to whoever called the function.

```python
def add_numbers(a, b):
    answer = a + b
    return answer # Hand the answer back!

# The function runs, returns the answer (15), and stores it in my_result
my_result = add_numbers(10, 5) 
print(my_result) # Prints: 15
```

When we build our User Interface, we will write functions that `return` the final predictions to the screen!
