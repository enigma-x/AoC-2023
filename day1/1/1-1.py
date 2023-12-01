# AoC-2023 // Day1-1
import re
numberlist = []

def find_first_number(input,rev=False):
    if rev is True:
        input = input[::-1]
    m = re.search(r"\d", input)
    if m:
        return input[m.start()]
    else:
        pass
      
with open('input', 'r', encoding='UTF8') as reader:
    line = reader.readline()
    while line != '':
        first = find_first_number(line)
        last = find_first_number(line,rev=True)
        number=(first +last)
        numberlist.append(int(number))
        line = reader.readline()

print(sum(numberlist))