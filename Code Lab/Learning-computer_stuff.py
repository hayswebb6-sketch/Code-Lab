import random
import ctypes
import webbrowser
import time
import urllib.parse
import subprocess
def generated_error():
    while True:
        x=random.randrange(1,15001)
        Error="Error Code: "+str(ctypes.WinError(x))
        if "<no description>"not in str(Error):
            print("Process failed\n")
            print(f"{Error} | Hex: 0x{x:08X}")
            time.sleep(1)
            webbrowser.open("https://www.google.com/search?q="+urllib.parse.quote_plus(f"How to fix Windows error {x} {ctypes.WinError(x).strerror}"),new=0)
            time.sleep(15)
            subprocess.Popen([r"C:\Users\Hays\AppData\Local\Programs\Microsoft VS Code\Code.exe", "--reuse-window"])
            break
        else:
            continue
generated_error()