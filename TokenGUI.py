import json
import tkinter as tk

token = None

root = tk.Tk()
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


def saveToken():
    temp = text.get(0.0, tk.END)
    temp = temp.strip("\n")
    if str(temp).startswith("pk_"):
        global token
        token = temp

        js = {"Authorization": temp}
        with open("tk.json", "w") as file:
            json.dump(js, file)

        label["text"] = "Zapisano Token"
        root.destroy()
        root.quit()
    else:
        label["text"] = "Nieprawidłowy token, podaj inny"


Button = tk.Button(
    master=root, text="Zapisz token", font=("SEGOEUIL", "15"), command=saveToken
).pack(fill=tk.X)


def getToken():
    root.mainloop()
    if token != None:
        return token
    else:
        print("Brak tokenu")
        exit()
