# AoC-2023 // Day2-2
# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

powers_games = []

with open('input', 'r', encoding='UTF8') as reader:
    line = reader.readline()
    while line != '':
        red = []
        green = []
        blue = []
        
        # split the line
        split_line = (line.split("\n"))[0]
        
        # get GameID
        gameID = ((split_line.split(":"))[0].split(" "))[1]
                        
        # split sets
        sets = (split_line.split(":"))[1].split(";")
    
        # iterate each draw for this set
        for draw in sets:
            cubes = draw.split(",")

            # determine amount and color of cubes
            for determine in cubes:
                x = determine.split(" ")

                amount = x[1]
                color = x[2]
                
                if color == "red":
                    red.append(int(amount))
                if color == "blue":
                    blue.append(int(amount))
                if color == "green":
                    green.append(int(amount))

        x = max(red)*max(green)*max(blue)
        powers_games.append(int(x))
        line = reader.readline()

print(sum(powers_games))
