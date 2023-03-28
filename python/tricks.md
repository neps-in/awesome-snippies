# 1. Avoid Nested Python Loops Using product() Function

# Old way

```
list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]

for a in list_a:
    for b in list_b:
        for c in list_c:
            if a + b + c == 2077:
                print(a, b, c)

```

# Pythonic way
# To make it neater and cleaner, we can use the product() function, which is from the itertools module, to optimise the code:

```
from itertools import product

list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]

for a, b, c in product(list_a, list_b, list_c):
    if a + b + c == 2077:
        print(a, b, c)
# 70 2000 7
```

# 2. Walrus Operator

Walrus Operator: A Cute Trick for Assignment Expressions
Since Python 3.8, there is a new syntax called “walrus operator” that can assign values to variables as part of a larger expression.

The operator := got its cute name from the eyes and tusks of a walrus.

# This syntax is very easy to understand. For instance, if we would like to write the following two lines of Python code in one line, how to do it?

```
author = "Yang"
print(author)
# Yang
```

Unfortunately, we cannot directly put the assignment into the print() function. There will be a TypeError if we try it:

```
print(author="Yang")
# TypeError: 'author' is an invalid keyword argument for print()
```

Thanks to the walrus operator, we can really do this in one line:

```
print(author:="Yang")
# Yang
```

# 3. Ternary Conditional Operator: Writing a Simple If-Else Structure in One Line

```py
# Old way
if a<b:
  min = a
else:
  min = b

# Pythonic way
min = a if a < b else b

```

# 4. Using Lambda Functions To Define Simple Functions

If you only want to define a simple function, probably you don’t need to use the traditional syntax for it. The lambda function is a more elegant option.

For example, the following function is to calculate the Fibonacci numbers:

## Old way
```py
def fib(x):
    if x<=1:
        return x
    else:
        return fib(x-1) + fib(x-2)
```

It works perfectly but the code itself is a bit ugly. Let’s write a one-liner to implement the same function:

## Pythonic way
```py
fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
```

# 5. List Comprehensions: Get a List in a Pythonic Way

To say the list comprehension makes your code elegant is still an understatement. It can save you lots of typing and time but still keep your code readable. Few programming languages can do this.

```py
Genius = ["Jerry", "Jack", "tom", "yang"]
L1 = [name if name.startswith('y') else 'Not Genius' for name in Genius]
print(L1)
# ['Not Genius', 'Not Genius', 'Not Genius', 'yang']
```

# 6. Leveraging the Higher-Order Functions in Python

Python has some built-in higher-order functions that give us the convenience to write some common logic.

For example, the map() function is a famous and frequently-used higher-order function. It receives two parameters, one is a function and the other is an iterable. Executing the map function will apply the function to each element of the iterable.

```py
names = ['yAnG', 'MASk', 'thoMas', 'LISA']
names = map(str.capitalize, names)
print(list(names))
# ['Yang', 'Mask', 'Thomas', 'Lisa']
```

As the above example shows, with the help of the map() function, we can avoid writing a for loop to capitalize every word in the names list.

Another famous higher-order function is reduce(). As its name implies, it applies a function into an iterable and does the cumulative operation for it.

For instance, the following example converts a list into one string:

```py
from functools import reduce

city = ['L', 'o', 'n', 'd', 'o', 'n', 2, 0, 2, 0]
city_to_str = reduce(lambda x, y: str(x) + str(y), city)
print(city_to_str)
# London2020

```

# 7. Union Operators: The Easiest Way To Merge Dictionaries

Merging dictionaries is a common requirement in daily Python programming. There are many ways to do it. But all of them were ugly before Python 3.9.

Since Python 3.9, we finally got the most elegant way for dictionary merging — using union operators.

```py
cities_us = {'New York City': 'US', 'Los Angeles': 'US'}
cities_uk = {'London': 'UK', 'Birmingham': 'UK'}

cities = cities_us|cities_uk
print(cities)
# {'New York City': 'US', 'Los Angeles': 'US', 'London': 'UK', 'Birmingham': 'UK'}
```

As the above example shows, we can simply use the | operator to merge the two different dictionaries. Even more, it also supports in-place merging:

```py
cities_us = {'New York City': 'US', 'Los Angeles': 'US'}
cities_uk = {'London': 'UK', 'Birmingham': 'UK'}

cities_us |= cities_uk
print(cities_us)
# {'New York City': 'US', 'Los Angeles': 'US', 'London': 'UK', 'Birmingham': 'UK'}
```

# 8. F-Strings: The Pythonic String Formatting Technique

Almost every programming language supports string formatting syntax. But not each one is as elegant as Python’s f-string technique.

```py
pi = 3.1415926
print(f'Pi is approximately equal to {pi:.2f}')
# Pi is approximately equal to 3.14

id = 1  # need to print a 3-digit number
print(f"The id is {id:03d}")
# The id is 001

N = 1000000000  # need to add separator
print(f'His networth is ${N:,d}')
# His networth is $1,000,000,000
```

As the above program displays, using the f-string trick, we can apply a Python variable and define its format specifications inside an f-string.

Can you remember the string formatting syntax of the C programming language? Do you agree that Python’s f-string syntax is much simpler? 🌞

>
> “Simple is better than complex.” — The Zen of Python
>

What makes the f-string technique more stunning is that we can embed expressions inside f-strings. The embed expressions will be evaluated at run time.

The following example will print the time of today with the help of an f-string:

```py
from datetime import datetime

print(f"Today is {datetime.today()}")
# Today is 2021-07-31 18:20:48.956829
```

# 9. Using Asterisks for Unpacking Iterables and Destructuring Assignments
How to merge a list, a tuple and a set into one list?

The most elegant way is using asterisks:

```py
A = [1, 2, 3]
B = (4, 5, 6)
C = {7, 8, 9}
L = [*A, *B, *C]
print(L)
# [1, 2, 3, 4, 5, 6, 8, 9, 7]
```

As stated above, the asterisks can be used as prefixes of iterables to unpack their items.

Besides unpacking iterables, the asterisks can also be used for destructuring assignments in Python:

```py
a, *mid, b = [1, 2, 3, 4, 5, 6]
print(a, mid, b)
# 1 [2, 3, 4, 5] 6
```

As shown above, with the help of one asterisk, the mid variable receives the items in the middle as a list.







