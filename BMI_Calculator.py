from tkinter import *

win = Tk()
win.minsize(height=300, width=300)
win.config(padx=50, pady=50)


def calculate_it():
    height = height_input.get()
    weight = weight_input.get()

    if height == "" or weight == "":
        bmi_label.config(text= "Enter your height and weight")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text= "Invalid height or weight")



height_label = Label(text="Enter your height(cm)")
height_input = Entry()
height_label.pack()
height_input.pack()


weight_label = Label(text="Enter your weight(kg)")
weight_input = Entry()
weight_label.pack()
weight_input.pack()

result_label = Label(text="Result:")
result_label.pack()

calculate_button = Button(text="Calculate", command=calculate_it)
calculate_button.pack()

bmi_label = Label()
bmi_label.pack()

def write_result(bmi):
    result_string = f"Your bmi is : {round(bmi,2)} you are : "
    if bmi <= 16:
        result_string += "Severely Thin"

    elif 16 < bmi <= 17:
        result_string += "Moderately Thin"

    elif 17 < bmi <= 18.5:
        result_string += "Mild Thin"

    elif 18.5 < bmi <= 25:
        result_string += "Normal"

    elif 25 < bmi <= 30:
        result_string += "Overweight"

    elif 30 < bmi <= 35:
        result_string += "Obese class 1"

    elif 35 < bmi <= 40:
        result_string += "Obese class 2"

    else:
        result_string += "Obese class 3"
    return result_string

win.mainloop()
