#Scope in action 
def test():
    y = 10
    return y

#print(y)

""" Traceback (most recent call last):
  File "/Users/almirasd/python_class/python-intro-homework/week-6/assignment-6/warmup3.py", line 6, in <module>
    print(y)
NameError: name 'y' is not defined """


x = test()
print(x)

