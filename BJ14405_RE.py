import re

exp = '((pi)*(ka)*(chu)*)+'
result = re.fullmatch(exp, input())

print('YES') if result else print('NO')
