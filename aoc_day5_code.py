# --- Day 5: Supply Stacks ---
# The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.
#
# The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.
#
# The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.
#
# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:
#
#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.
#
# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:
#
# [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:
#
#         [Z]
#         [N]
#     [C] [D]
#     [M] [P]
#  1   2   3
# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:
#
#         [Z]
#         [N]
# [M]     [D]
# [C]     [P]
#  1   2   3
# Finally, one crate is moved from stack 1 to stack 2:
#
#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.
#
# After the rearrangement procedure completes, what crate ends up on top of each stack?
# 
# Your puzzle answer was VCTFTJQCG.
#
# --- Part Two ---
# As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.
#
# Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.
#
# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.
#
# Again considering the example above, the crates begin in the same configuration:
#
#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
# Moving a single crate from stack 2 to stack 1 behaves the same as before:
#
# [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
# However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:
#
#         [D]
#         [N]
#     [C] [Z]
#     [M] [P]
#  1   2   3
# Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:
#
#         [D]
#         [N]
# [C]     [Z]
# [M]     [P]
#  1   2   3
# Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:
#
#         [D]
#         [N]
#         [Z]
# [M] [C] [P]
#  1   2   3
# In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.
#
# Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
#
# Your puzzle answer was GCFGLDNJZ.
#
# Both parts of this puzzle are complete! They provide two gold stars: **
#
# At this point, you should return to your Advent calendar and try another puzzle.
#
# If you still want to see it, you can get your puzzle input.
#
# You can also [Share] this puzzle.

starting_dict = {
    1: ["Q", "M", "G", "C", "L"],
    2: ["R", "D", "L", "C", "T", "F", "H", "G"],
    3: ["V", "J", "F", "N", "M", "T", "W", "R"],
    4: ["J", "F", "D", "V", "Q", "P"],
    5: ["N", "F", "M", "S", "L", "B", "T"],
    6: ["R", "N", "V", "H", "C", "D", "P"],
    7: ["H", "C", "T"],
    8: ["G", "S", "J", "V", "Z", "N", "H", "P"],
    9: ["Z", "F", "H", "G"],
}

#     [G] [R]                 [P]
#     [H] [W]     [T] [P]     [H]
#     [F] [T] [P] [B] [D]     [N]
# [L] [T] [M] [Q] [L] [C]     [Z]
# [C] [C] [N] [V] [S] [H]     [V] [G]
# [G] [L] [F] [D] [M] [V] [T] [J] [H]
# [M] [D] [J] [F] [F] [N] [C] [S] [F]
# [Q] [R] [V] [J] [N] [R] [H] [G] [Z]
#  1   2   3   4   5   6   7   8   9
def get_piece_to_move(how_many: int, start_stack):
    index_to_start_from = (len(start_stack) - how_many)
    total = start_stack[index_to_start_from:]
    if len(total) != how_many:
        print("ERROR!")
    return total


def move_the_stack(letter_stack, chart, start, end):
    for letter in letter_stack:
        # add letters to new stack
        chart[end].append(letter)

        # remove last entry to starting array
        chart[start] = chart[start][:-1]


def do_the_thing():
    f = open("aoc_day5_data.py", "r")
    lines = f.readlines()

    moves = [line[:-1] for line in lines]

    copy_of_start = starting_dict.copy()
    for move in moves:
        current_move = move.split(' ')

        # GET PIECES
        num_to_move = int(current_move[1])
        stack_to_take_from = int(current_move[3])
        destination_stack = int(current_move[5])
        start_stack = copy_of_start[stack_to_take_from]

        # get piece to move
        piece_to_move = get_piece_to_move(num_to_move, start_stack)

        # Part 2 i just had to comment out this line so the piece wouldn't flip
        # piece_to_move.reverse()  # leave in for part 1

        move_the_stack(piece_to_move, copy_of_start, stack_to_take_from, destination_stack)

    last_letters = ''
    all_keys = copy_of_start.keys()  # [1, 2, ..., 9]
    for key in all_keys:
        index = len(copy_of_start[key]) - 1
        last_letter = copy_of_start[key][index]
        last_letters += last_letter

    print(last_letters)


if __name__ == "__main__":
    do_the_thing()
