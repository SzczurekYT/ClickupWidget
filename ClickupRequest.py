import requests as rq
import json
import datetime


def getData(toVar):

    try:
        with open("tk.json", "r") as file:
            headers = json.load(file)
    except FileNotFoundError:
        print("Token File not found?")
        exit()

    headers["Authorization"] = str(headers["Authorization"]).replace("\n", "")

    print("Getting all workspaces")

    url = "https://api.clickup.com/api/v2/team"
    workspaces = rq.get(url=url, headers=headers).json()

    print("Getting tasks")

    allTasks = []

    for workspace in workspaces["teams"]:
        insert = workspace["id"]
        url = f"https://api.clickup.com/api/v2/team/{insert}/task?page=0"
        request = rq.get(url=url, headers=headers).json()
        allTasks += request["tasks"]

    filteredTasks = []

    print("Filtering data")

    today = datetime.date.today()

    for task in allTasks:
        if task["start_date"] == None:
            if task["due_date"] != None:
                if datetime.date.fromtimestamp(int(task["due_date"]) / 1000) == today:
                    filteredTasks.append(task)
        else:
            if datetime.date.fromtimestamp(int(task["start_date"]) / 1000) <= today:
                if task["due_date"] != None:
                    if (
                        datetime.date.fromtimestamp(int(task["due_date"]) / 1000)
                        >= today
                    ):
                        filteredTasks.append(task)
                else:
                    filteredTasks.append(task)

    print("Saving data")
    if toVar != True:
        with open("tasks.json", "w") as file:
            json.dump(filteredTasks, file, indent=4)
    else:
        return filteredTasks
