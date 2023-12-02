import re

regx = r'(\d|one|two|three|four|five|six|seven|eight|nine|zero).*(\d|one|two|three|four|five|six|seven|eight|nine|zero)'
rb = '.?([0-9]|one|two|three|four|five|six|seven|eight|nine|zero)'

with open('./input.txt') as f:
    data = f.read()

sum = 0


def get_num(match):
    if match is None:
        return ''
    if '0' <= match <= '9':
        return match
    match match:
        case "one":
            return '1'
        case "two":
            return '2'
        case "three":
            return '3'
        case "four":
            return '4'
        case "five":
            return '5'
        case "six":
            return '6'
        case "seven":
            return '7'
        case "eight":
            return '8'
        case "nine":
            return '9'
        case "zero":
            return '0'
    return ''


for line in data.split("\n"):
    match = re.search(regx, line.lower())
    if match is not None and len(match.groups()) == 2:
        sum += int(f"""{get_num(match.group(1))}{get_num(match.group(2))}""")
    elif match is None:
        match = re.search(rb, line)
        if match is not None:
            sum += int(f"""{get_num(match[1])}{get_num(match[1])}""")

#
print(f"""The sum is {sum}""")
