# Romb of start

n = 4

"""
   *    # spaces n-1, stars:1
  * *   # spaces n-2, stars:2 
 * * *  # spaces n-1, stars:3
* * * * # spaces 0, stars: 4(n)
 * * *
  * *
   *

"""


def print_line(spaces_count, stars_count):
    line_spaces = ''.join([' '] * spaces)
    line_stars = ' '.join(['*'] * stars)
    print(line_spaces + line_stars)




for i in range(n):
    spaces = n - i - 1
    stars = i + 1
    print_line(spaces,stars)

for i in range(n - 2, -1, -1):
    spaces = n - i - 1
    stars = i + 1
    print_line(spaces,stars)
