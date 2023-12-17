import customtkinter
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("700x500")

# variables needed for this project
# gender = male/female
# weight in kg
# height in cm
# age in years

# activity level:
# not active(1.4): Works a desk job, very little activity outside of lifting
# lightly active(1.7): Works a desk job, takes pet for a walk most days in addition to lifting
# moderately active(1.9): Works as a full-time waitress, occasionally plays tennis in addition to lifting
# highly active(2.1): Works as a construction worker, regular hiking in addition to lifting

# BMR (MALE) = 10 X WEIGHT(KG) + 6.25 X HEIGHT(CM) - 5 X AGE(Y) + 5
# BMR (FEMALE) = 10 X WEIGHT(KG) + 6.25 X HEIGHT(CM) - 5 X AGE(Y) - 161


class Person:
    def __init__(self, age=0, weight=0, height=0, gender="", activity=""):
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.activity = activity
        
    def calculate_macros(self):
        if not self.age or not self.weight or not self.height:
            messagebox.showinfo("Error", "Please fill in all the information")
            return
        
        if not self.gender or not self.activity:
            messagebox.showinfo("Error", "Please fill in all the information")
            return
        
        if self.gender == "Male":
            formula = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
            print(formula)
            
        elif self.gender == "Female":
            formula = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
            print(formula)
        
        else:
            messagebox.showinfo("Error", "Please fill in all the required fields.")
            return
        
person = Person()

def calculate():
    person.__init__(
        int(age_entry.get()),
        int(weight_entry.get()),
        int(height_entry.get()),
        str(gender_combobox.get()),
        str(activity_combobox.get())
    )
    person.calculate_macros()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Macro Calculator")
label.pack(pady=12, padx=10)

gendermenu_var = customtkinter.StringVar(value="")
gender_combobox = customtkinter.CTkComboBox(master=frame, values=["Male", "Female"], variable=gendermenu_var)
gender_combobox.pack(pady=12, padx=10)

activity_var = customtkinter.StringVar(value="")
activity_combobox = customtkinter.CTkComboBox(master=frame, values=["Not Active", "Lightly Active", "Moderately Active", "Highly Active"], variable=activity_var)
activity_combobox.pack(pady=12, padx=10)

age_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Age")
age_entry.pack(pady=12, padx=10)
weight_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Weight in kg")
weight_entry.pack(pady=12, padx=10)
height_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Height in cm")
height_entry.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Calculate", command=calculate)
button.pack(pady=12, padx=10)


root.mainloop()