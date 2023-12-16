import json
import os
import time


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def load_zoo(ZOO_PATH):
    try:
        # Try to open the file for reading
        with open(ZOO_PATH, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        cls()
        # Handle the case where the file doesn't exist
        data = []
        print(f"creating {ZOO_PATH}...")
        with open(ZOO_PATH, "w") as file:
            json.dump(data, file, indent=2)
    except json.JSONDecodeError:
        # Handle the case where the file has invalid JSON
        print(f"The file at {ZOO_PATH} contains invalid JSON.")
        data = []
        print(f"reseting {ZOO_PATH} to []")
        with open(ZOO_PATH, "w") as file:
            json.dump(data, file, indent=2)
    # else: # Handle other potential exceptions or perform additional actions
    finally:
        return data


def input_validator(inp: str):
    if len(inp) == 1 and inp.isdigit() and 0 < int(inp) < 7:
        print(inp)
        return inp
    else:
        return 0


def dsp_menu(Act, zoo):
    time.sleep(1)
    print("\n###zoo app###\n")
    if len(zoo) == 0:
        for act in Act:
            if act.value in [1, 3, 6]:
                print(f"{act.name} --> {act.value}")
        act = input("\nselect an action: ")
        act = input_validator(act)
        if act != 0:
            return Act(int(act))
        else:
            return 0
    else:
        for act in Act:
            print(f"{act.name} --> {act.value}")
        act = input("\nselect an action: ")
        act = input_validator(act)
        if act != 0:
            return Act(int(act))
        else:
            return 0


def print_zoo(zoo: list[dict]):
    cls()
    if len(zoo) == 0:
        print("db is empty, add some animals...")
    else:
        for idx, animal in enumerate(zoo):
            print(idx, animal)


def search(zoo: list[dict]):
    cls()
    print_zoo(zoo)
    print("\n")
    search_key = input("enter search key: ")
    search_value = input("enter search value: ")
    search_result = [
        animal
        for animal in zoo
        if search_key in animal and animal[search_key] == search_value
    ]
    print("\n")
    for result in search_result:
        print(result)


def add(zoo: list[dict], ZOO_PATH):
    cls()
    zoo.append(
        {
            "type": input("enter type: "),
            "name": input("name: "),
            "age": input("age: "),
        }
    )
    with open(ZOO_PATH, "w") as file:
        json.dump(zoo, file, indent=2)


def update(zoo: list[dict], ZOO_PATH):
    print_zoo(zoo)
    print("\n")
    upd_idx = int(input("select animal index: "))
    zoo[upd_idx] = {
        "type": input("enter type: "),
        "name": input("name: "),
        "age": input("age: "),
    }
    print_zoo(zoo)
    with open(ZOO_PATH, "w") as file:
        json.dump(zoo, file, indent=2)


def delete(zoo: list[dict], ZOO_PATH):
    print_zoo(zoo)
    del_idx = int(input("\nselect animal index: "))
    if 0 <= del_idx < len(zoo):
        del zoo[del_idx]
    print_zoo(zoo)
    with open(ZOO_PATH, "w") as file:
        json.dump(zoo, file, indent=2)


def ext():
    cls()
    print("FIN")
    exit()
