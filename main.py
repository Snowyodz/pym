#############################################
#https://github.com/Fryghtened/pym
#############################################

#####################################################
#BY Fry#5607 ON DISCORD DM FOR COPYRIGHT USAGE :) <3
#####################################################

#############################################
#FUNCTIONS
#############################################


def While(condition , body):
    while condition:
        exec(body)

def If(condition = "",body = "",elsee = "",eliff = "", elifbody = ""):
    if condition:
        exec(body)
    elif eliff:
        exec(elifbody)
    else:
        exec(elsee)

def For(condition, condition2 ,body):
    for condition in condition2:
        exec(body)

def Print(printt):
    print(printt)

def Exec(execc):
    exec(execc)

def Sum(*args):
    print(sum(args))

def Diff(a,b):
    print(a-b)

def Mult(a,b):
    print(a*b)

def Div(a,b):
    print(a/b)

def Return(body):
    return body

def Pass():
    pass

def Len(body):
    print(len(body))
#############################################
#DO FUNCTIONS
#############################################

def doWhile():
    While(True , """
a = 10
if a > 9:
    print(a)
    """)

def doIf():
    a = 0
    If(a == 10,"""print("hi")""" , """print(":(")""" , a == 1 , """print(":)")""")

def doFor():
    list = [1,2,3,4 , "hi"]
    For("" , list , """print("hi")""")

def doPrint():
    b = "Fry"
    a = f"His name is {b},Poggers"
    Print(a)

def doExec():
    a = """print("what's up?")"""
    Exec(a)

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

def doReturn():
    print(Return(10))

def doPass():
    Pass()

def doLen():
    listt = [1,2,3,4,5,6,7,8,9,10,11,12]
    Len(listt)
#############################################
#CALL THEM OWO UWU
#############################################
#doWhile()
#doIf()
#doFor()
#doPrint()
#doExec()
#doSum()
#doDiff()
#doMult()
#doDiv()
#doReturn()
#doPass()
#doLen()

