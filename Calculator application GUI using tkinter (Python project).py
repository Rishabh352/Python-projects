from tkinter import * # import everything from tkinter module

win = Tk() # This is to create a basic GUI window
win.geometry("312x324")  # This is for the size of the GUI window 
win.resizable(0, 0)  # This is to prevent from resizing the GUI window
win.title("Calculator") # This is to set the title of the GUI window

###################Starting with functions ####################
# 'btn_click' function : 
# This Function continuously updates the input field whenever you enter a number

def btn_click(item):
    global expression     # point out the global expression variable
    expression = expression + str(item)   # concatenation of string
    input_text.set(expression)   # update the expression by using set method

# 'bt_clear' function :This is used to clear the input field

def bt_clear(): 
    global expression  #point out the global expression variable
    expression = ""  #initialize the expression variable  by empty string
    input_text.set("") #update the expression by using set method
 
# 'bt_equal':This method calculates the expression present in input field
 
def bt_equal():
    global expression  #point out the global expression variable
    result = str(eval(expression)) # 'eval':This function is used to evaluate the string expression directly
    input_text.set(result) #update the result by using set method
    expression = ""   #initialize the expression variable  by empty string

    expression = ""   # globally declare the expression variable
 
 
# 'StringVar()' :It is used to get the instance of input field
 
input_text = StringVar() # StringVar() is the variable class
 
# Let us create a frame for the input field
#highlightbackground: This option used to represent the thickness of the focus highlight.
#highlightcolor: This option used to represent the color of the focus highlight when the frame has the focus.
 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="white", highlightthickness=2) #The Frame widget is used as a container widget to organize other widgets.
 
input_frame.pack(side=TOP) # Pack Organizes widgets in horizontal and vertical boxes that are limited to left, right, top, bottom positions. Each box is offset and relative to each other.
 
#Let us create a input field inside the 'Frame'
 
input_field = Entry(input_frame, font=('arial', 25, 'bold'), textvariable=input_text, width=50, bg="white", justify = RIGHT) # justify:This option is used to define how to align multiple lines of text. We can Use LEFT, RIGHT, or CENTER as its values.
 
input_field.pack(ipady=5) # 'ipady' is internal padding to increase the height of input field
 
#Let us create another 'Frame' for the button below the 'input_frame'
 
btns_frame = Frame(win, width=312, height=272.5, bg="grey") #The Frame widget is used as a container widget to organize other widgets.
 
btns_frame.pack()  # Pack Organizes widgets in horizontal and vertical boxes that are limited to left, right, top, bottom positions. Each box is offset and relative to each other.
 
 

# Lambda Functions is referred to as Anonymous Function in Python
# It allow us to send multiple data through the callback function
# In Button Command, lambda is used to pass the data to a callback function.
# bg: This option used to represent the normal background color displayed behind the label and indicator.
# bd: This option used to represent the size of the border around the indicator and the default value is 2 pixels.
# cursor: By using this option, the mouse cursor will change to that pattern when it is over the frame.
# column: The column to put widget in.
# columnspan : How many columns widget occupies.

# first row
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3,bd = 0, bg = "light grey", cursor = "hand2", command = lambda: bt_clear())
clear.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1) 
 
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3,bd = 0, bg = "light grey", cursor = "hand2", command = lambda: btn_click("/"))
divide.grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row
 
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3,bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(7))
seven.grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3,bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(8))
eight.grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3,bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(9))
nine.grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3,bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("*"))
multiply.grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3,bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(4))
four.grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3,bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(5))
five.grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3,bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(6))
six.grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3,bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("-"))
minus.grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3,bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(1))
one.grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3,bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(2))
two.grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3,bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(3))
three.grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3,bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("+"))
plus.grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fifth row
 
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3,bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(0))
zero.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 # padx puts some space between the button widgets and between the closeButton and the right border of the root window
 # pady puts some space between the button widgets and the borders of the frame and the borders of the root window.
 # The Grid geometry manager puts the widgets in a 2-dimensional table
 # The master widget is split into a number of rows and columns, and each “cell” in the resulting table can hold a widget.
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3,bd = 0, bg = "light grey", cursor = "hand2", command = lambda: btn_click("."))
point.grid(row = 4, column = 2, padx = 2, pady = 2)
 
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3,bd = 0, bg = "light grey", cursor = "hand2", command = lambda: bt_equal())
equals.grid(row = 4, column = 3, padx = 1, pady = 1)

#start the GUI
win.mainloop()
