# Day 1 - Module 1: Core Python Basics (30 mins)

Welcome to your journey into Machine Learning! We are starting from absolute zero. If you've never typed a line of code before, you are in the right place.

## 1. What is Python? (5 mins)
Think of Python as a language you use to give instructions to your computer. A computer is incredibly fast but incredibly literal; it only does exactly what you tell it. Python is the language we use to tell it what to do.

## 2. Variables and Data Types (10 mins)
A **variable** is simply a labeled box where you can store information. When we build our app, we'll need boxes to hold numbers (like temperature) and boxes to hold text.

There are three main types of data we care about right now:
- **Integers:** Whole numbers (e.g., `25`)
- **Floats:** Decimal numbers (e.g., `40.5`)
- **Strings:** Text, always wrapped in quotes (e.g., `"London"`)

```python
temperature = 25       # This is an integer
humidity = 40.5        # This is a float
city = "London"        # This is a string
```

## 3. Comments (`#`) (5 mins)
Sometimes you want to write a note to yourself in the code, but you don't want the computer to try and run it as an instruction. You do this using the `#` symbol. Anything after the `#` on that line is ignored by the computer.

```python
# This is a comment! The computer ignores this.
aqi = 100 # This creates a variable called aqi
```

## 4. The `print()` Statement & Strings (10 mins)
How do you know what the computer is doing? You ask it to talk to you! The `print()` command tells the computer to display whatever is inside the parentheses on your screen.

```python
print("Hello world!")
# The screen will display: Hello world!

temperature = 25
print(temperature)
# The screen will display: 25
```

### String Concatenation and Type Casting
What if you want to print text AND a number together? You cannot mathematically add the word "The temperature is " to the number `25`. 

To fix this, we have to disguise the number as text using `str()`. This is called **Type Casting**. Once both are text, adding them together glues them side-by-side (**Concatenation**).

```python
temperature = 25
# Disguise the number 25 as the text "25", then glue them together
print("The temperature is " + str(temperature)) 
# The screen displays: The temperature is 25
```
