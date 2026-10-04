#Imports: tkinter(Which is the standard GUI library for Python applications)
import tkinter as tk
#root=tk.Tk() means creating the main application window for the Tkinter GUI
root = tk.Tk()
root.title("Learning Tkinter")
root.geometry("400x300")
root.configure(bg="black")

#A label widget displays text on the GUI
label=tk.Label(root, text="Text", fg="brown", bg="black")
#The pack() method is used to add the label widget to the GUI and specify its padding
label.pack(pady=20)
#A button widget allows the user to interact with the GUI by clicking it
#The lambda function is used to pass the command to the button without executing it immediately
#Fg means foreground color
#Bg means background color
button=tk.Button(root, text="Button", fg="yellow", bg="black")
button.pack(pady=10)

#The mainloop() function starts the Tkinter event loop, which runs the GUI application
root.mainloop()