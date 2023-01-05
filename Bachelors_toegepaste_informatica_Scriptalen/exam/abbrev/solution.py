# Write your solution in this file
import re

with open('input.txt','r') as f:
    lines = f.readlines()
    pattern = "(([a-z])([a-z]{6,})([a-z]))"

    with open('output.txt', 'w') as d:
        for line in lines:
            result = re.findall(pattern, line)
            newline = line
            for i in result:
                sizeString = str(i[1] + str(len(i[2])) + i[3])
                newline = re.sub(pattern, sizeString, newline, count=1)
            d.write(newline)

