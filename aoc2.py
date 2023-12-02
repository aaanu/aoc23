import re

# return indexes of all appearances of char in string
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

with open('./Downloads/input.txt', 'r') as input:
    data = input.readlines()
    max_red = 12
    max_green = 13
    max_blue = 14
    str_red = "red"
    str_blue = "blue"
    str_green = "green"
    sum_of_game_ids = 0
    for line in data:
        key, val = line.split(":", 1)
        _, game_id_str = key.split(" ", 1)
        combos = val.split(";") # combos = [" 1 blue, 19 red, 5 green", "8 green, 6 red, 18 blue", ...]
        red_totals = []
        blue_totals = []
        green_totals = []
        for combo in combos: # combo = " 1 blue, 19 red, 5 green"
            combo = combo.replace(" ", "") # remove all whitespace. combo now looks like "1blue,19red,5green"
            # look for string color. look for comma before it. if no comma, go from beginning of string til index of color.
            comma_indexes = find(combo, ",")
            try:
                red_index = combo.index(str_red)
            except ValueError as e:
                red_index = None
            if red_index:
                comma_index = [x for x in comma_indexes if x < red_index] # can be length 0 1 or 2
                if len(comma_index) == 0:
                    # its at the beginning of the string
                    red_total = combo[:red_index]
                    red_totals.append(int(red_total))
                elif len(comma_index) == 1:
                    # its the middle or last element
                    comma_index = comma_index[0]
                    red_total = combo[comma_index+1:red_index]
                    red_totals.append(int(red_total))
                else:
                    # its the last element
                    comma_index = comma_index[1]
                    red_total = combo[comma_index+1:red_index]
                    red_totals.append(int(red_total))
            try:
                blue_index = combo.index(str_blue)
            except ValueError as e:
                blue_index = None
            if blue_index:
                comma_index = [x for x in comma_indexes if x < blue_index] # can be length 0 1 or 2
                if len(comma_index) == 0:
                    # its at the beginning of the string
                    blue_total = combo[:blue_index]
                    blue_totals.append(int(blue_total))
                elif len(comma_index) == 1:
                    # its the middle or last element
                    comma_index = comma_index[0]
                    blue_total = combo[comma_index+1:blue_index]
                    blue_totals.append(int(blue_total))
                else:
                    # its the last element
                    comma_index = comma_index[1]
                    blue_total = combo[comma_index+1:blue_index]
                    blue_totals.append(int(blue_total))
            try:
                green_index = combo.index(str_green)
            except ValueError as e:
                green_index = None
            if green_index:
                comma_index = [x for x in comma_indexes if x < green_index] # can be length 0 1 or 2
                if len(comma_index) == 0:
                    # its at the beginning of the string
                    green_total = combo[:green_index]
                    green_totals.append(int(green_total))
                elif len(comma_index) == 1:
                    # its the middle or last element
                    comma_index = comma_index[0]
                    green_total = combo[comma_index+1:green_index]
                    green_totals.append(int(green_total))
                else:
                    # its the last element
                    comma_index = comma_index[1]
                    green_total = combo[comma_index+1:green_index]
                    green_totals.append(int(green_total))
        if all(t <= max_red for t in red_totals) and all(t <= max_blue for t in blue_totals) and all(t <= max_green for t in green_totals):
            game_id = int(game_id_str)
            sum_of_game_ids += game_id
    print(sum_of_game_ids)
