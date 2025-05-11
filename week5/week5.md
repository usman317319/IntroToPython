# Week 5
## Array
An array is a collection of values stored in consecutive memory locations. In c++, arrays are quite complex with the array name as being the pointer pointing to the address of the 1st element in that array. And dealing with address of 2D array is a whole new world. Python is very different from C/C++ and abstracts away many low-level computational details, allowing the programmer to focus more on what to do rather than how to do it. This power of python will be very visible as we study arrays in Python.

## Lists
An array (Collection of values) is called a list in Python. List can store multiple values.
```
[2, 5, 6]
```
There's no need to specify the datatype, the size of a list. And lists are expandable as much as needed.
Not only that but a python list can hold different datatypes.
```
[0.2, "This is a string inside a list", 3, [65, "List inside the list"], True]
```
Indexing in list is done the same way as done in c++ arrays i.e. the 1st element has index 0 and so on.
```
[0.2, "This is a string inside a list", 3, [65, "List inside the list"], True][1]
```
would return the string `"This is a string inside a list"`.

## Function
A function is a set of code which in normal execution is ignored until the function is explicitly called.
```
def func(x):
    return x*x
```
Function is declared with the keyword `def`, followed by the function name, and function arguments inside of the brackets. As can be seen, no-where the datatype (return datatype) of function can be seen. Same goes for the argument, there is no datatype. This is very different from C/C++.