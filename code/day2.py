
def part_1(val_list):
    x = 0
    y = 0
    for val in val_list:
        val_unpacked = val.split(" ")
        direction = val_unpacked[0]
        magnitude = val_unpacked[1]
        if direction == "forward":
            x += int(magnitude)
        elif direction == "down":
            y += int(magnitude)
        else:
            y -= int(magnitude)
    return x * y

def part_2(val_list):
    x = 0
    y = 0
    aim = 0
    for val in val_list:
        val_unpacked = val.split(" ")
        direction = val_unpacked[0]
        magnitude = val_unpacked[1]
        if direction == "forward":
            y += aim * int(magnitude)
            x += int(magnitude)
        elif direction == "down":
            aim += int(magnitude)
        else:
            aim -= int(magnitude)
    return x * y





if __name__ == "__main__":
    f = open("advent-of-code-2021/input/day2.txt", "r").read()
    vals = f.split("\n")
    vals = [v for v in vals if len(v) > 0]
    prod = part_1(vals)
    print(f"part 1 solution is {prod}")
    prod2 = part_2(vals)
    print(f"part 2 solution is {prod2}")