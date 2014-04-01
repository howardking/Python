# Moduler Ari

num = 49
ones = num % 10
print ones

hour = 20
shift = 8

print 'hour = ', (hour + shift) % 24


width = 800
position = 3
move = -5
position = (position + move) % width

print position

hour = 3
ones = hour % 10
tens = hour / 10
print tens, ones, ":00"
print str(tens), str(ones), ":00"
print str(tens) + str(ones) + ":00"

# import simplegui
import math
import random

print math.pi
