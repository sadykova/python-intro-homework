#Calculate years since graduation
#grad_year=input("What year did you graduate?") Code with bug
grad_year = int(input("What year did you graduate?"))
print(f"You graduated {2026-grad_year} year(s) ago!")

#Error message
""" Traceback (most recent call last):
  File "/Users/almirasd/python_class/python-intro-homework/week-2/assignment-2/warmup4.py", line 2, in <module>
    print(f"You graduated {2026-grad_year} year(s) ago!")
TypeError: unsupported operand type(s) for -: 'int' and 'str' """

#Error: Data type error. Didn't convert year into integer. When this step is missed, then input is assumed to be string.
#Fix: Fixed by explicitly converting input into integer.
