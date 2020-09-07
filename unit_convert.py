# Done by Carlos Amaral (01/09/2020)

from tkinter import *
from functools import partial

window = Tk()
window.title("Unit-length converter")
window.geometry("400x205")



# Define a global variable
length_val = "Meters"

# Define drop list
def store_length(set_length):
    global length_val
    length_val = set_length

def command_convert(rlabel, rlabel2, inputn):

    if length_val == 'Meters':
        # Conversion of Meters to Inches
        inches = round(float(inputn.get()) * 39.3701,2)
        rlabel.config(text=str(inches) +' Inches')

        # Conversion of meters to feet
        feet = round(float(inputn.get()) * 3.281,2)
        rlabel2.config(text=str(feet) + ' Feet')


    elif length_val == 'Inches':
        # Conversion of Inches to Meters
        meters = round(float(inputn.get()) / 39.3701,2)
        rlabel.config(text=str(meters) + ' Meters')

        # Conversion of inches to feet
        feet = round(float(inputn.get()) / 12,2)
        rlabel2.config(text=str(feet) + ' Feet')


    elif length_val == 'Feet':
        # Conversion of feet to meters
        meters = round(float(inputn.get()) / 3.281,2)
        rlabel.config(text=str(meters) + ' Meters')

        # Conversion of feet to inches
        inches = round(float(inputn.get()) * 12,2)
        rlabel2.config(text=str(inches) + ' Inches')
    return


var = StringVar()


# Create input label
label_entry = Label(window, text="Enter length", font=('bold', 12), pady=20)
label_entry.grid(row=1, column=0)


# Create label for result
label_result = Label(window)
label_result.grid(row=3, column=1)
label_result2 = Label(window)
label_result2.grid(row=4, column=1)

# Create text box
inputlength = StringVar()
entry_length = Entry(window, textvariable=inputlength)
entry_length.grid(row=1, column=1)


# Create Convert Button
command_convert = partial(command_convert, label_result, label_result2, inputlength)
convert_button = Button(window, text="Convert", width=11, command=command_convert)
convert_button.grid(row=1, column=2)


# Create a dropdown list
dropList = ['Meters', 'Inches', 'Feet']
drop = OptionMenu(window, var, *dropList, command=store_length)
var.set(dropList[0])
drop.grid(row=2, column=1)

window.mainloop()