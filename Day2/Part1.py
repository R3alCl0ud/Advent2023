import re

with open('./input.txt') as f:
    data = f.read()

regx = r"(\d*) ?(red|green|blue)"


sumID = 0

for line in data.split('\n'):
    add = True
    parts = line.split(": ")[1].split('; ')
    gameID = int(line.split(": ")[0].split(' ')[1])
    for part in parts:
        if add is False:
            continue
        red = 0
        green = 0
        blue = 0
        cubes = part.split(', ')
        for cube in cubes:
            search = re.search(regx, cube.lower())
            # print(search[1])
            match search[2]:
                case "red":
                    red += int(search[1])
                case "green":
                    green += int(search[1])
                case "blue":
                    blue += int(search[1])
        # print(cubes)
        if red > 12 or green > 13 or blue > 14:
            print(cubes)
            add = False
            continue
    if add:
        sumID += gameID

print("sum of IDs:", sumID)