import getpass
import json
import tkinter as tk
from getpass import getuser


def getToken():

    root = tk.Tk()
    root.config(width=15)
    # root.geometry("500x150")

    frame = tk.Frame(master=root, relief=tk.RAISED, borderwidth=1, bg="White")
    frame.pack(fill=tk.X)

    label = tk.Label(
        master=frame,
        text="Podaj osobisty token ClickupAPI",
        font=("SEGOEUIL", "15", "bold"),
        bg="White",
    )
    label.pack()

    text = tk.Text(
        master=root,
        bg="White",
        relief=tk.RIDGE,
        borderwidth=1,
        height=1,
        width=75,
        font=("SEGOEUIL", "15"),
    )
    text.pack(fill=tk.BOTH)

    global succes
    succes = False

    def saveToken():
        token = text.get(0.0, tk.END)
        token = token.replace("\n", "")
        if str(token).startswith("pk_"):

            user = getuser()
            js = {"Authorization": token}
            with open(
                f"C:\\Users\\{user}\\AppData\\Local\\ClickupWidget\\tk.json", "w"
            ) as file:
                json.dump(js, file)

            print("Token Saved")
            label["text"] = "Zapisano Token"

            global succes
            succes = True
            root.destroy()
            root.quit()
        else:
            label["text"] = "Nieprawidłowy token, podaj inny"

    Button = tk.Button(
        master=root, text="Zapisz token", font=("SEGOEUIL", "15"), command=saveToken
    ).pack(fill=tk.X)

    root.mainloop()
    return succes
