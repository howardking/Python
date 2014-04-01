# This program is used to excerise debug

import random

def volume_cube(side):
	return side ** 3

s = 2
print "Volume of cube with side", s, "is", volume_cube(s), "."

def random_dice():
	die1 = random.randint(1, 6)
	die2 = random.randint(2, 8)
	print die1, die2
	return die1 + die2

print "Sum of two random dice, rolled once:", random_dice()
print "Sum of two randon dice, rolled again:", random_dice()

import math

def volume_sphere(radius):
	return float(4) / 3 * math.pi * (radius ** 3)

r = 2
print "Volume of sphere of radius", r, "is", volume_sphere(r), "." 

def area_triangle(base, height):
	return float(1) / 2 * base * height

b = 5
h = 4

print "Area of triangle with base", b, "and height", h, "is", area_triangle(b, h), "."
