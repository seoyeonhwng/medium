import re

s = input()
while s:
    if s.startswith('pi'):
        s = s[2:]
    elif s.startswith('ka'):
        s = s[2:]
    elif s.startswith('chu'):
        s = s[3:]
    else:
        break

print('YES') if len(s) == 0 else print('NO')
