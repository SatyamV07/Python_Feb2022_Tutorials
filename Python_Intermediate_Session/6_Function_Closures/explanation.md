# Python Inner and Closure Functions

&nbsp;
### In this course we learn about

```
1. Defining inner functions
2. Using inner functions as helper functions
3. Building function closures
4. Using captured variables in a closure
5. Captured data functions in a closure
6. Decorators - We discuss as a seperate topic later
```

### Overview

```
1. Python supports procedural, object oriented and functional programming
2. Functional Programming relies on functions in the way the object oriented programming relies on objects 
3. Closures are a way of wrapping data with a function
4. Closures use an inner function and capture variables to encapsulate execution and data
5. Inner functions are functions defined within functions
6. Decorators are a special case of closures where you use functions to wrap the execution to other functions
```

### *Inner Function Definition*
```
A function defined inside another function is known as an inner function or a nested function. 
In Python, this kind of function can access names in the enclosing function.

The core feature of inner functions is their ability to access variables and objects 
from their enclosing function even after this function has returned. 

The use cases of Python inner functions are varied. You can use them to provide encapsulation 
and hide your functions from external access, you can write helper inner functions, 
and you can also create closures and decorators. In this section, you’ll learn about the 
former two use cases of inner functions, and in later sections, you’ll learn how to create closure 
factory functions and decorators.
```

### *Closure Definition*
 
```
Closures are dynamically created functions that are returned by other functions. 
Their main feature is that they have full access to the variables and names defined 
in the local namespace where the closure was created, even though the enclosing function 
has returned and finished executing.
```
&nbsp;

:rewind: [Back to Main Menu](https://github.com/kumar1987an/Python_Sept2021_Tutorials/blob/root/README.md)
