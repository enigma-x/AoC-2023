# AoC-2023 // Day1-2
import re
numberlist = []

def find_digit_indexes(input):
    digit_indexes = []
    regex_list = [r"1", r"2", r"3", r"4", r"5", r"6", r"7", r"8", r"9", r"one", r"two", r"three", r"four", r"five", r"six", r"seven", r"eight", r"nine"]
    for regex_item in regex_list:
        m = [m.start() for m in re.finditer(regex_item, input)]
        if m:
            for item in m:
                if regex_item == "one":
                    value = 1
                elif regex_item == "two":
                    value = 2
                elif regex_item == "three":
                    value = 3
                elif regex_item == "four":
                    value = 4
                elif regex_item == "five":
                    value = 5
                elif regex_item == "six":
                    value = 6
                elif regex_item == "seven":
                    value = 7
                elif regex_item == "eight":
                    value = 8
                elif regex_item == "nine":
                    value = 9
                else:
                    value = regex_item
                digit_indexes.append([item, value])
            digit_indexes.sort(key = lambda x: x[0])
    return digit_indexes
        
with open('input', 'r', encoding='UTF8') as reader:
    line = reader.readline()
    while line != '':
        current_digit_indexes = []
        digit_indexes = find_digit_indexes(line)
        thenumber = (str(digit_indexes[0][1]) +str(digit_indexes[-1:][0][1]))
        numberlist.append(int(thenumber))
        line = reader.readline()

print(sum(numberlist))