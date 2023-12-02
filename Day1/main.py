import re

with open('./input.txt') as f:
    data = f.read()

sum = 0

for line in data.split("\n"):
    start = ''
    end = ''
    for c in line:
        if line == '':
            start = ''
        elif ('0' <= c <= '9') or (True):
            if start == '':
                start = c
            else:
                end = c
    if end == '':
        end = start
    if f'''{start}{end}''' != '':
        sum += int((f'''{start}{end}'''))

print(sum)