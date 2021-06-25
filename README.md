Improving python for the better.

Adding my own functions to python.

DOCS 

1) if
2) else
3) elif

```
def doIf():
    a = 0
    If(a == 10,"""print("hi")""" , """print(":(")""" , a == 1 , """print(":)")""")
```

Here the first set of arguments is the If. This contains 
a) The condition,
b) The body.
The body must be a string
```
"""
print("Yo")
"""
```
For example above ```a==10``` is the condition which is a Truthy and returns a bool, ```True``` or ```False```. If it's true the first arguemnent get's executed.
If false the second one get's executed. Again the 4th argument is a Truth and if it returns a True the last arguement get's executed. Only one elif is allowed.


4) while

```
def doWhile():
    While(True , """
a = 10
if a > 9:
    print(a)
    """)
```

The ```While()``` contains two arguements. The condition and the body. It is executed in such a way given below

```
while condition:
  body
```

Condition can be a normal python condition such as ```True``` , ```False``` , ```not done``` , etc. The body needs to be a string for example
```
"""
print("OwO")
"""
```

5) for
6) print
7) exec
8) Sum
9) Diff
10) Multiply
11) Divide
12) return
13) pass
14) len
15) Raise
16) exit