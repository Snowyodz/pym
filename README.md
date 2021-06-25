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

```
def doFor():
    list = [1,2,3,4 , "hi"]
    For("i" , list , """print("hi")""")
```

The for work like shown below

```
for condition1 in condition2:
    body
```

The first arguement is the condition 1 forexample ```i```, it then adds a ```in```  during execution. You can then use condition2, for example, ```range(100)``` or ```list``` or you can also use ```"list```. Basically it's normal syntax but more screwed.

6) print

Print is the easiest.

```
def doPrint():
    b = "Fry"
    a = f"His name is {b},Poggers"
    Print(a)
```

Like above the syntax is very simple, ```Print(what_to_print)```, you can use any data types, str , int , float etc.

7) exec

Exec syntax is also very very easy.

```
def doExec():
    a = """print("what's up?")"""
    Exec(a)

```

You can use a variable or you can also just use a long string like below
```
def doExec():
    Exec("""print("what's up?")""")
```

8) Sum
9) Diff
10) Multiply
11) Divide

The above is shown as below

```
def doSum():
    Sum(1,2,3,4,6,2,6,2,7,2,6,2958,2968,1)

def doDiff():
    a = 100
    b = 99
    Diff(100,99)

def doMult():
    Mult(100,4)


def doDiv():
    Div(100,2)
```

You can sum any finite number values, difference two values, multiply two values and divide two values.

12) return

Return is prety broken at the moment but you can use such syntax for now.

```
def doReturn():
    print(Return(10))
```

13) pass

This is the easiest one.

```
def doPass():
    Pass()
```
14) len

```
def doLen():
    listt = [1,2,3,4,5,6,7,8,9,10,11,12]
    Len(listt)
```
Use a str,list,arr.

15) Raise

```
def doRaise():
    if 10 < 100:
        Raise(TypeError,"100 is greater than 10.")
def doRaise():
    if 10 < 100:
        Raise(ValueError,"100 is greater than 10.")
```

16) exit

```
def doExit():
    count = 0
    while True:
        print("YAY")
        count += 1
        if count == 10:
            Exit()
```

The above example is for testing that I used but you can simply just ```Exit()``` and well it exits.