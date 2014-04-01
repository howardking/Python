# Starting point for calculator

import simplegui

# Initialize globals
store = 0
operand = 0

# Define functions that manipulate store and operand
def output():
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
def swap():
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    global store, operand
    store = store + operand
    output()
    
def sub():
    global store, operand
    store = store - operand
    output()

def multiply():
    global store, operand
    store = store * operand
    output()
    
def div():
    global store, operand
    store = float(store) / operand
    output()
    
    
def enter(inp):
    global operand
    operand = float(inp)
    output()
frame = simplegui.create_frame("Caculator", 200, 500)

frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)
frame.add_button("Mul", multiply, 100)
frame.add_button("Div", div, 100)
frame.add_input("Enter operand", enter, 100)

frame.start()

