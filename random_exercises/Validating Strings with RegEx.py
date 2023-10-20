import re

strings = ['a', 'b', 'ab', 'ba', 'aba']

regularExpression = r'^[a-z]$|^([a-z]).*\1$'

for string in strings:
    if re.match(regularExpression, string):
        print(True)
    else:
        print(False)    

