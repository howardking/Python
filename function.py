# function excise

#  computes the area of a triangle

def triangle_area(base, height):
    area = float(1) / 2 * base * height
    return area

area = triangle_area(10, 30)

print area

# converts fahrenheit to cesius

def fahrenheit2celsius(fahrenheit):
    celsius = (float(5) / 9) * (fahrenheit - 32)
    return celsius

# test 
c1 = fahrenheit2celsius(32)
c2 = fahrenheit2celsius(212)
print c1,    c2

# converts fahrenheit to kelvin
def fahrenheit2kelvin(fahrenheit):
	celsius = fahrenheit2celsius(fahrenheit)
	kelvin = celsius + 273.15
	return kelvin

# test
k1 = fahrenheit2kelvin(32)
k2 = fahrenheit2kelvin(212)
print k1, k2

def   hello():
	print "hello world"

# test
hello()
h = hello()
print h
