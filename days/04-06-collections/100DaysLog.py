import os
from collections import namedtuple, defaultdict
from itertools import islice


def main():
    data_file = os.path.join(".\\", "100DaysLOG.txt")
    Days = namedtuple("Days", "Day Date Created Learned")

    lines = []
    with open(data_file, encoding='utf-8') as file:
        lines = file.readlines()[2:] # gets rid of comment and blank line

    data = []
    for line in lines[2:]:
        items = line.split("|")[1:5]
        d = Days(Day=items[0].strip(), Date=items[1].strip(), Created=items[2].strip(), Learned=items[3].strip())
        data.append(d)

    for t in data:
        print(t)
        print()

    return


if __name__ == "__main__":
    main()
