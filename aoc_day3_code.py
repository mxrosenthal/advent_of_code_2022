priorities = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}


def make_the_groups(data):
    group_dict = {}
    group = []
    i = 0
    j = 1

    for line in data:
        group_name = "group " + str(j)
        if i < 3:
            group.append(line)
            i += 1
        if i == 3:
            group_dict[group_name] = group
            group = []
            i = 0
            j += 1
    return group_dict


def find_common_letter(data):
    first = data[0]
    second = data[1]
    third = data[2]

    for letter in first:
        if second.find(letter) != -1 and third.find(letter) != -1:
            # print('returning: ', letter)
            return letter

    for letter in second:
        if first.find(letter) != -1 and third.find(letter) != -1:
            # print('returning: ', letter)
            return letter

    for letter in third:
        if second.find(letter) != -1 and first.find(letter) != -1:
            # print('returning: ', letter)
            return letter

    # print(first, second, third)
    print("Letter Not found")


def do_the_second_thing():
    f = open("aoc_day3_data.py", "r")
    lines = f.readlines()
    lines = [line[:-1] for line in lines]
    groups = make_the_groups(lines)
    print(groups)
    priorities_sum = 0
    for group in groups:

        # print("group: ", group)
        common_letter = find_common_letter(groups[group])
        priority = priorities[common_letter]
        priorities_sum += priority

    print(priorities_sum)


def do_the_thing():
    f = open("aoc_day3_data.py", "r")
    lines = f.readlines()
    lines = [line[:-1] for line in lines]
    priority_sum = 0
    # print(lines[0])

    # i = 0
    for line in lines:
        # if i > 2:
        #     continue

        midpoint = int(len(line) / 2)
        # print(midpoint)
        first_half = line[0:midpoint]
        second_half = line[midpoint : len(line)]
        # print("1: ", first_half)
        # print("2: ", second_half)
        letter_found = False

        for letter in first_half:
            if not letter_found:
                if letter in second_half:
                    # print(letter)
                    priority = priorities[letter]
                    # print(priority)
                    priority_sum += priority
                    # print(priority_sum)
                    letter_found = True
        # i += 1
    print("total: ", priority_sum)
    # print(lines[0])


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    # do_the_thing()
    do_the_second_thing()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
