import re

with open('./input.txt') as f:
    data = f.read()

regx = r"(\d*) ?(red|green|blue)"

sumID = 0

for game in data.split('\n'):
    grabs = game.split(": ")[1].split('; ')
    gameID = int(game.split(": ")[0].split(' ')[1])
    red = 0
    green = 0
    blue = 0
    for grab in grabs:
        cubes = grab.split(', ')
        for cube in cubes:
            search = re.search(regx, cube.lower())
            match search[2]:
                case "red":
                    red = max(int(search[1]), red)
                case "green":
                    green = max(int(search[1]), green)
                case "blue":
                    blue = max(int(search[1]), blue)
    power = red * green * blue
    sumID += power

print("sum of IDs:", sumID)
