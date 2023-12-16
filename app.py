from enum import Enum

import mdl


class Act(Enum):
    PRINT = 1
    SEARCH = 2
    ADD = 3
    UPDATE = 4
    DEL = 5
    EXT = 6


ZOO_PATH = "zoo.json"
mdl.cls()


def main():
    try:
        while 1:
            zoo = mdl.load_zoo(ZOO_PATH)
            act = mdl.dsp_menu(Act, zoo)
            if act == Act.PRINT:
                mdl.print_zoo(zoo)
            elif act == Act.SEARCH:
                mdl.search(zoo)
            elif act == Act.ADD:
                mdl.add(zoo, ZOO_PATH)
            elif act == Act.UPDATE:
                mdl.update(zoo, ZOO_PATH)
            elif act == Act.DEL:
                mdl.delete(zoo, ZOO_PATH)
            elif act == Act.EXT:
                mdl.ext()
            else:
                print("invalid input, select only 1-6 buttons...")

    except KeyboardInterrupt:
        print("\nFIN")
        exit()


if __name__ == "__main__":
    main()
