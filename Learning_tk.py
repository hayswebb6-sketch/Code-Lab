import tkinter as tk

root = tk.Tk()
root.title("Learning Tkinter")
root.geometry("400x300")
root.configure(bg="black")


label=tk.Label(root, text="Non-Changed Text", fg="brown", bg="black")
label.config(text="Non-Changed Text")
label.pack(pady=20)
button=tk.Button(root, text="Change Text", fg="green", bg="black", command=lambda: label.config(text="I changed!"))
button.pack(pady=10)

root.mainloop()