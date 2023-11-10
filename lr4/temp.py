import re

reg = '\w*ac\w*'
print(re.findall(reg, input("input your text ==> ")))

input()