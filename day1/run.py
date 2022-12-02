# part 1
with open('day1_input.txt', mode='r', encoding='utf-8-sig') as f:
    lines = f.readlines()

    # store max seen
    max_cals = 0

    # store current elf calorie count
    current_count = 0
    for l in lines:
        line = l.strip("\n")

        if line == "":
            max_cals = max(max_cals, current_count)
            current_count = 0
        else:
            num = int(line)
            current_count += num

    print(max_cals)


with open('day1_input.txt', mode='r', encoding='utf-8-sig') as f:
    lines = f.readlines()

    elf_cal_list = []

    # store current elf calorie count
    current_count = 0
    for l in lines:
        line = l.strip("\n")

        if line == "":
            elf_cal_list.append(current_count)
            current_count = 0
        else:
            num = int(line)
            current_count += num

    elf_cal_list.sort(reverse=True)

    top_three_sum = sum(elf_cal_list[:3])

    print(top_three_sum)
