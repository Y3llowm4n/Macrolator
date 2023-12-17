import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def calculate():
    print("Here are your macro's")
    


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Macro's Calculater")
label.pack(pady=12, padx=10)
       
entry1 = customtkinter.CTkEntry     (master=frame, placeholder_text="Age")
entry1.pack(pady=12, padx=10)         
entry2 = customtkinter.CTkEntry     (master=frame, placeholder_text="Weight")
entry2.pack(pady=12, padx=10) 

button = customtkinter.CTkButton(master=frame, text="Login", command=calculate )
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()