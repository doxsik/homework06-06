from datetime import datetime, time
import os
from time import sleep 
from itertools import cycle

clear = lambda: os.system('cls')

one = """\u2B1B\u2B1B  
  \u2B1B  
  \u2B1B  
  \u2B1B  
  \u2B1B  
  \u2B1B  
\u2B1B\u2B1B\u2B1B"""

two = """\u2B1B\u2B1B\u2B1B
\u2B1B  \u2B1B
    \u2B1B
\u2B1B\u2B1B\u2B1B
\u2B1B    
\u2B1B    
\u2B1B\u2B1B\u2B1B"""

three = """\u2B1B\u2B1B\u2B1B
    \u2B1B
    \u2B1B
\u2B1B\u2B1B\u2B1B
    \u2B1B
    \u2B1B
\u2B1B\u2B1B\u2B1B"""

four = """\u2B1B  \u2B1B
\u2B1B  \u2B1B
\u2B1B  \u2B1B
\u2B1B\u2B1B\u2B1B
    \u2B1B
    \u2B1B
    \u2B1B"""

five = """\u2B1B\u2B1B\u2B1B
\u2B1B    
\u2B1B    
\u2B1B\u2B1B\u2B1B
    \u2B1B
    \u2B1B
\u2B1B\u2B1B\u2B1B"""

six = """\u2B1B\u2B1B\u2B1B
\u2B1B    
\u2B1B    
\u2B1B\u2B1B\u2B1B
\u2B1B  \u2B1B
\u2B1B  \u2B1B
\u2B1B\u2B1B\u2B1B"""

seven = """\u2B1B\u2B1B\u2B1B
    \u2B1B
    \u2B1B
    \u2B1B
    \u2B1B
    \u2B1B
    \u2B1B"""

eight = """\u2B1B\u2B1B\u2B1B
\u2B1B  \u2B1B
\u2B1B  \u2B1B
\u2B1B\u2B1B\u2B1B
\u2B1B  \u2B1B
\u2B1B  \u2B1B
\u2B1B\u2B1B\u2B1B"""

nine = """\u2B1B\u2B1B\u2B1B
\u2B1B  \u2B1B
\u2B1B  \u2B1B
\u2B1B\u2B1B\u2B1B
    \u2B1B
    \u2B1B
\u2B1B\u2B1B\u2B1B"""

zero = """\u2B1B\u2B1B\u2B1B
\u2B1B  \u2B1B
\u2B1B  \u2B1B
\u2B1B  \u2B1B
\u2B1B  \u2B1B
\u2B1B  \u2B1B
\u2B1B\u2B1B\u2B1B
"""

empty_colum = ["  ", "  ", "  ", "  ", "  ", "  ", "  "]

tuple_of_numbers = (zero, one, two, three, four, five, six, seven, eight, nine)
colors = ('\U0001f7e6', '\U0001f7ea', '\U0001f7e9', '\U0001f7e8')
color = cycle(colors)

counter = 0
plus_minus = 1

while True:
    colored = next(color)
    point = colored
    colored_numbers = [number.replace('\u2B1B', colored) for number in tuple_of_numbers]
    origen_watch = datetime.now()
    watch = origen_watch.strftime('%H%M%S')
    watch_in_numbers = [colored_numbers[int(number)] for number in watch]

    first, second, third, fourth, fifth, sixth = watch_in_numbers
    
    colum = empty_colum.copy()
    colum[counter] = point
    counter += plus_minus
    if counter == 6:
        plus_minus = (-1)
    elif counter == 0:
        plus_minus = 1

    print(first.split("\n")[0] + "  " + second.split("\n")[0] + "  " + colum[0] + "  " + third.split("\n")[0]\
        + "  " + fourth.split("\n")[0] + "  " + colum[0] + "  " + fifth.split("\n")[0] + "  " + sixth.split("\n")[0])

    print(first.split("\n")[1] + "  " + second.split("\n")[1] + "  " + colum[1] + "  " + third.split("\n")[1]\
        + "  " + fourth.split("\n")[1] + "  " + colum[1] + "  " + fifth.split("\n")[1] + "  " + sixth.split("\n")[1])

    print(first.split("\n")[2] + "  " + second.split("\n")[2] + "  " + colum[2] + "  " + third.split("\n")[2]\
        + "  " + fourth.split("\n")[2] + "  " + colum[2] + "  " + fifth.split("\n")[2] + "  " + sixth.split("\n")[2])

    print(first.split("\n")[3] + "  " + second.split("\n")[3] + "  " + colum[3] + "  " + third.split("\n")[3]\
        + "  " + fourth.split("\n")[3] + "  " + colum[3] + "  " + fifth.split("\n")[3] + "  " + sixth.split("\n")[3])

    print(first.split("\n")[4] + "  " + second.split("\n")[4] + "  " + colum[4] + "  " + third.split("\n")[4]\
        + "  " + fourth.split("\n")[4] + "  " + colum[4] + "  " + fifth.split("\n")[4] + "  " + sixth.split("\n")[4])

    print(first.split("\n")[5] + "  " + second.split("\n")[5] + "  " + colum[5] + "  " + third.split("\n")[5]\
        + "  " + fourth.split("\n")[5] + "  " + colum[5] + "  " + fifth.split("\n")[5] + "  " + sixth.split("\n")[5])

    print(first.split("\n")[6] + "  " + second.split("\n")[6] + "  " + colum[6] + "  " + third.split("\n")[6]\
        + "  " + fourth.split("\n")[6] + "  " + colum[6] + "  " + fifth.split("\n")[6] + "  " + sixth.split("\n")[6])
    
    sleep(1)
    
    clear()