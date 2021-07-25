from pathlib import Path
import tkinter as tk
import json
import ClickupRequest as CR
from TokenGUI import getToken
from getpass import getuser

user = getuser()

# Check if there is file containing Clickup API Token.
# If it exists print to log that everything is fine.
# Else show to user a GUI that will allow him to enter token.
token_file = Path(f"C:\\Users\\{user}\\AppData\\Local\\ClickupWidget\\tk.json")
if token_file.is_file():
    print("Token file exists!")
else:
    print("Token file not found, asking user to enter token.")
    if getToken() != True:
        print("Error occured, no token, closing!")
        exit()

# Get tasks data
tasks = CR.getData(True)

# Basic TKInter window setup
win = tk.Tk()
win.attributes("-topmost", True)
win.overrideredirect(True)

# Try to open file with windows settings
try:
    with open(
        f"C:\\Users\\{user}\\AppData\\Local\\ClickupWidget\\window.json", "r"
    ) as file:
        locs = json.load(file)
        x = locs["x"]
        y = locs["y"]
        height = locs["height"]
        width = locs["width"]

# If it don't exist then use default settings
except FileNotFoundError:
    ws = win.winfo_screenwidth()  # width of the screen
    hs = win.winfo_screenheight()  # height of the screen

    # Set window initial height and width
    height = 800
    width = 600

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (width / 2)
    y = (hs / 2) - (height / 2)

# Set the window location and size
win.geometry("%dx%d+%d+%d" % (width, height, x, y))

# Create Frame for buttons
buttons = tk.Frame(win, bg="White")
buttons.pack(side=tk.TOP, fill=tk.X)

# Define function for saving window location and size
def saveLoc():
    with open("window.json", "w") as file:
        data = {
            "x": win.winfo_x(),
            "y": win.winfo_y(),
            "height": win.winfo_height(),
            "width": win.winfo_width(),
        }
        json.dump(data, file)


# Create button for saving window location and size
btn_save_loc = tk.Button(buttons, text="Save Location", command=saveLoc)
btn_save_loc.pack(side=tk.LEFT)

# Define function for toggling ability to edit window
def switchMode():
    if win.overrideredirect() == True:
        win.overrideredirect(False)
        btn_mode["text"] = "Leave Edit Mode"
    else:
        win.overrideredirect(True)
        btn_mode["text"] = "Edit Mode"


# Create button for toggling ability to edit window
btn_mode = tk.Button(buttons, text="Edit Mode", command=switchMode)
btn_mode.pack(side=tk.LEFT)

# def updateTasks
# i = 0
# while i < 2:
#     try:
#         with open("tasks.json", "r") as file:
#             tasks = json.load(file)
#             break
#     except FileNotFoundError:
#         i += 1
#         print("File with tasks not found.")
#         print("Trying to get data")
#         CR.getData(False)


# Create button for quitting the application
btn_exit = tk.Button(buttons, text="Exit", command=win.quit)
btn_exit.pack(side=tk.RIGHT)

# Create Frame for "Tasks" label
frame = tk.Frame(master=win, relief=tk.RAISED, borderwidth=3, bg="White")
frame.pack(fill=tk.X)

# Create "Tasks" label
label = tk.Label(
    master=frame, text="Taski:", font=("SEGOEUIL", "20", "bold"), bg="White"
)
label.pack()

# Create empty list for widgets
widgets = []

# Create widget for each task
for task in tasks:
    frame = tk.Frame(master=win, relief=tk.RIDGE, borderwidth=1, bg="White")
    frame.pack(fill=tk.X)
    label = tk.Label(
        master=frame, text=task["name"], font=("SEGOEUIL", "18"), bg="White"
    )
    label.pack()

# Run the app
win.mainloop()
