# Week 4
## Input
Input from terminal can be received using `input()` function in python. `input()` accepts an argument which may be a string, int or float. Then  performs the following operations:
- Writes the argument to standard output
- Reads from the standard input of the terminal until the next line character is reached
- Returns the received input as a string
And that's all with `input()`.

## Writing Returned string from `input()` to `stdout`
```
input("Enter")
```
The above line of code will successfully read input from `stdin` and `return` it. The next task is to display the string to the user or more precisely write the string to the standard output stream (`stdout`).
```
print(input("Enter"))
```
> Bonus Task: Is it possible to write the returned string from `input()` function to `stdout` without using `print()` function?

More than one inputs can be received as follows
```
print(input("Enter n1: "), input("Enter n2: "))
```

## Language of Standard Input Stream and Standard Output Stream
`print()` and `input()` function kind of automate what is done in `c++` using `cout` and `cin` statements. Let's study which of `cout`, `cin` statements are invoked when `print()` and `input()` function are called.
```
input("Enter")
```
<br><br><br><br><br><br>
The flow of the above statement is as follows
|Function|In Program Action|Terminal|
|--------|-----------------|--------|
| input() | Writes | stdout |
| input() | Reads | stdin |
| input() | Returns | |

Similarly for a more complex statement
```
print(input("Enter"))
```
|Function|In Program Action|Terminal|
|--------|-----------------|--------|
| input() | Writes | stdout |
| input() | Reads | stdin |
| input() | Returns | |
|print()| Writes | stdout |

## String Concatenation
Concatenation is just a fancy word for combining or adding up two strings to make a single string. Therefore
```
>>> "a" + "b"
'ab'
```
Combining the strings `"a"` and `"b"` makes them `"ab"`. This operation is called string concatenation.
```
>>> print(input("Enter n1:") + input("Enter n2:"))
Enter n1:2
Enter n2:3
23
```
Although the expected answer was 5, the answer received is 23. This happened because `input()` always returns string. Therefore, + operator operated on two strings performs string concatenation and 23 is written to `stdout` as a string. So how do integer addition can be perform on data returned by input()?

## Type Conversion
Strings can be converted to integers (but not all!) using `int()` function. `int()` function accepts an arugment (a string) and returns an integer. Therefore, in order to perform integer addition on data received from `input()`
```
>>> print(int(input("Enter n1:")) + int(input("Enter n2:")))
Enter n1:2
Enter n2:3
5
```
Now that there are two integers on both sides of the `+` operator, integer addition is performed.

## Variables
Any defined integer, float, string, function etc all are saved in computer main memory (RAM). As explained in earlier lectures, an application level process requests the Operating System to assign some memory to store it's values.
```
5
```
The above written statement is a fully function python script. Once this process is executed, it needs to store the integer `5` in computer's memory. The Operating System will assign the process that memory somewhere in the RAM, and the process will write `5` in that memory block. Now it is practically impossible to retrieve that `5` out of memory. Computer's Memory is so large, thousands of `5` maybe saved by different processes in the memory. Therefore, we can never exactly know where did the process saved that integer, so that we can reuse it.
Variables solve this issue. Variables keep track of memory where the process saved the integer.
```
x = 5
```
In the above python statement, `x` will point to the memory location where `5` is saved.

## Control Flow
Computer Programs have sequential flow. But there are situations where this behaviour needs to be changed. Flow of program can be controlled using `if ... else ...` and loops `for`, `while`.

## if else Statements in Python
`if else` block controls whether or not to execute one or more statement based on a condition.
```
if 1 == 1:
    print("1 is indeed equal to 1")
```
`==` comparison operator compare the objects and if they are same returns True, otherwise False. So we can see very clearly that `if` sees the True or False. It is not `if`'s responsibility to compare the two objects. `==` compares the two objects and return if they are same or not. Therefore, we can also write:
```
a = 1 == 1
if a:
    print("1 is indeed equal to 1")
```
`1==1` returns boolean value which is `True`, `True` is stored in computer's RAM and `a` keeps track of it in the memory. `if` sees there's a `True`, so the program executes the indented part of code. `indented`?
## Indentation
Indentation serves the same purpose which `{}` served in `C++`. That is, to specify these statements come under the hood of `if`. They are meant to be executed if and only if `if` receives a `True`. Indentation means 4 spaces before the python statement.
```
a = 1 == 1
if a:
    print("1 is indeed equal to 1")
    print("These statements are inside of if block")
print("This is outside of if block")
```
As soon as a statement starts from the very starting of a line, it is taken as a sequential python statement i.e. will be executed regardless of `if`.
