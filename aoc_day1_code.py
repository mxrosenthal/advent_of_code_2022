f = open("aoc_day1_data.py", "r")
lines = f.readlines()
edited_lines = [line[:-1] for line in lines]
# int_lines = [int(line) for line in edited_lines]
array_of_sums = []
current_sum = 0
for line in edited_lines:
    if line == '':
        array_of_sums.append(current_sum)
        current_sum = 0
        continue
    current_sum += int(line)

highest_value = max(array_of_sums)  # answer for part 1
array_of_sums.sort(reverse=True)
sum_of_top_three = 0
i = 0
for sum in array_of_sums:
    if i > 2:
        continue
    sum_of_top_three += sum
    i += 1

print(sum_of_top_three)  # answer for part 2