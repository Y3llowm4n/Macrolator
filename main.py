import customtkinter
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x600")

# Factors for the selected activity level
activity_factors = {
    "Not Active": 1.4,
    "Lightly Active": 1.7,
    "Moderately Active": 1.9,
    "Highly Active": 2.1
}

# Factors for the selected goal
goal_factors = {
    "Lose Weight": 0.85,
    "Maintain Weight": 1, 
    "Gain Weight": 1.15
}

# Class with all the attributes that a person need to give
class Person:
    def __init__(self, age=0, weight=0, height=0, gender="", activity="",goal=""):
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.activity = activity
        self.goal = goal
    
    # Calculation for calculating the macro's
    def calculate_macros(self):
        if not self.age or not self.weight or not self.height:
            messagebox.showinfo("Error", "Please fill in all the information")
            return
        
        if not self.gender or not self.activity:
            messagebox.showinfo("Error", "Please fill in all the information")
            return
        
        if self.gender == "Male":
            formula = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
            
        elif self.gender == "Female":
            formula = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
            
        else:
            messagebox.showinfo("Error", "Please fill in all the required fields.")
            return
        
        goal_factor = goal_factors.get(self.goal, 1.0)
        activity_factor = activity_factors.get(self.activity, 1.0)
        result = int(formula * activity_factor * goal_factor)
        messagebox.showinfo("Result", f"Calculated Macros: {result}") 
          
person = Person()

# Get all of the information out of the fields
def calculate():
    person.__init__(
        int(age_entry.get()),
        int(weight_entry.get()),
        int(height_entry.get()),
        str(gender_combobox.get()),
        str(activity_combobox.get()),
        str(goal_combobox.get())
    )
    
    person.calculate_macros()

# Main Frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Title of the Application
label = customtkinter.CTkLabel(master=frame, text="Macro Calculator")
label.pack(pady=12, padx=10)

# Box for selecting the gender of the user
gender_label = customtkinter.CTkLabel(master=frame, text="Select Gender:")
gender_label.pack(pady=5, padx=10)
gendermenu_var = customtkinter.StringVar(value="")
gender_combobox = customtkinter.CTkComboBox(master=frame, values=["Male", "Female"], variable=gendermenu_var)
gender_combobox.pack(pady=12, padx=10)

# Box for selecting the activity level of the user
activity_label = customtkinter.CTkLabel(master=frame, text="Select Activity Level:")
activity_label.pack(pady=5, padx=10)
activity_var = customtkinter.StringVar(value="")
activity_combobox = customtkinter.CTkComboBox(master=frame, values=["Not Active", "Lightly Active", "Moderately Active", "Highly Active"], variable=activity_var)
activity_combobox.pack(pady=12, padx=10)

# Box for selecting the goal of the user
goal_label = customtkinter.CTkLabel(master=frame, text="Select Goal:")
goal_label.pack(pady=5, padx=10)
goal_var = customtkinter.StringVar(value="")
goal_combobox = customtkinter.CTkComboBox(master=frame, values=["Lose Weight", "Maintain Weight", "Gain Weight"], variable=goal_var)
goal_combobox.pack(pady=12, padx=10)

# Input field for age
age_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Age")
age_entry.pack(pady=12, padx=10)

# Input field for weight
weight_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Weight in kg")
weight_entry.pack(pady=12, padx=10)

# Input field for height
height_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Height in cm")
height_entry.pack(pady=12, padx=10)

# Button for calculating macro's
button = customtkinter.CTkButton(master=frame, text="Calculate", command=calculate)
button.pack(pady=12, padx=10)

root.mainloop()