"""
1. Use all capital letter = PI = 3.14
2. Write constant in separate file. 
3. Use Final from typing module (Python 3.8+)
"""
# import constant

PI = 3.1416
print(PI)


import constant
print(constant.PI)


from typing import Final
PI: Final = 3.1416
print(PI)


PI = 3
print(PI)
