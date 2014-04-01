# global vs local variable

# num1 is a global variable

num1 = 1
print num1

# num2 is a local variable

def func():
    num1 = 2
    num2 = num1 + 1
    print num2
    
func()

print float(2)/3

print num1

def fahren_to_kelvin(fahren):
    celsius = float(5) / 9 * (fahren - 32)
    zero_celsius_in_kelvin = 273.15
    return celsius + zero_celsius_in_kelvin

print fahren_to_kelvin(32)
print fahren_to_kelvin(212)

num = 20

def func1():
    global num
    num += 1
    
def func2():
    global num
    num += 2
    
print num
func1()
print num
func2()
print num

