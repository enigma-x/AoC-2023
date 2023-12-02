# AoC-2023 // Day2-1
# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?

valid_games = []

with open('input', 'r', encoding='UTF8') as reader:
    line = reader.readline()
    while line != '':
        
        # split the line
        split_line = (line.split("\n"))[0]
        
        # get GameID
        gameID = ((split_line.split(":"))[0].split(" "))[1]
                        
        # split sets
        sets = (split_line.split(":"))[1].split(";")

        valid_draws = []
        
        # iterate each draw for this set
        for draw in sets:
        
            red = []
            green = []
            blue = []
        
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

                if (sum(red)) <= 12:
                    if (sum(green)) <= 13:
                        if (sum(blue)) <= 14:
                            valid_draws.append(1)
                        else:
                            valid_draws.append(0)
                    else:
                        valid_draws.append(0)
                else:
                    valid_draws.append(0)

        if 0 not in valid_draws:
            valid_games.append(int(gameID))
              
        line = reader.readline()

print(sum(valid_games))
