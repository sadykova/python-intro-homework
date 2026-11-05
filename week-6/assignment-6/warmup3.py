#Scope in action 
x = 0

def test():
    x = 10
    return x

print(test())
#print(x)
""" Traceback (most recent call last):
  File "/Users/almirasd/python_class/python-intro-homework/week-6/assignment-6/warmup3.py", line 7, in <module>
    print(x)
NameError: name 'x' is not defined """
