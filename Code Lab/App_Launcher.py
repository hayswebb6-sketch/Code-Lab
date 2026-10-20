import subprocess#Importing subprocess so that we can open other applications
import tkinter as tk#Importing tkinter so that we can create a GUI
from tkinter import messagebox#Importing messagebox from tkinter so that we can display messages to the user
import os#Importing os so that we can get the current working directory
import winreg#Importing winreg so that we can get the path of the applications


def open_notepad():
    subprocess.Popen(["notepad.exe"])#Opening notepad


def open_calculator():
    subprocess.Popen(["calc.exe"])#Opening calculator


def open_command_prompt():
    subprocess.Popen(["cmd.exe"], creationflags=subprocess.CREATE_NEW_CONSOLE)#Opening command prompt with a new console


def open_paint():
    subprocess.Popen(["mspaint.exe"])#Opening paint


def open_control_panel():
    subprocess.Popen(["control.exe"])#Opening control panel


def open_task_manager():
    subprocess.Popen(["taskmgr.exe"])#Opening task manager


def open_file_explorer():
    subprocess.Popen(["explorer.exe"])#Opening file explorer


def open_steam():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam")#Opening the registry key for steam
        steam, _ = winreg.QueryValueEx(key, "SteamExe")#Getting the path of the steam executable
        subprocess.Popen([steam])#Opening steam
    except OSError:#If the registry key does not exist
        steam = r"C:\Program Files (x86)\Steam\steam.exe"#Setting the path of the steam executable
        if os.path.isfile(steam):#If the file exists
            subprocess.Popen([steam])#Opening steam
        else:
            messagebox.showerror("Error", "Steam could not be found!")#Showing an error message


root = tk.Tk()#Creating the root window
root.title("App Launcher")
root.configure(bg="#0b0f0c")
font=("Consolas", 12, "bold")
title = tk.Label(root, text="APP LAUNCHER", font=("Consolas", 28, "bold"), fg="#39ff88", bg="#0b0f0c")
title.pack(pady=(50, 25))
frame = tk.Frame(root, bg="#0b0f0c")
frame.pack(expand=True, pady=(0, 80))

buttons = [
    ("Open Notepad", open_notepad),
    ("Open Calculator", open_calculator),
    ("Open Command Prompt", open_command_prompt),
    ("Open Paint", open_paint),
    ("Open Control Panel", open_control_panel),
    ("Open Task Manager", open_task_manager),
    ("Open File Explorer", open_file_explorer),
    ("Open Steam", open_steam),
]

for i, (text, command) in enumerate(buttons):
    tk.Button(
        frame,
        text=text,
        command=command,
        font=font,
        bg="#17251c",
        fg="#39ff88",
        activebackground="#39ff88",
        activeforeground="#0b0f0c",
        width=22,
        height=2,
        relief="flat",
        cursor="hand2",
    ).grid(row=i // 4, column=i % 4, pady=10, padx=10)
root.attributes("-fullscreen", True)
root.mainloop()