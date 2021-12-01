def part_a(input_list: list):
    greater_counter = 0
    for idx in range(1, len(input_list)):
        if input_list[idx] - input_list[idx-1] > 0:
            greater_counter += 1
    return greater_counter

def part_b(input_list: list):
    greater_counter = 0
    for idx in range(len(input_list)-3):
        if input_list[idx + 3] - input_list[idx] > 0:
            greater_counter += 1
    return greater_counter

if __name__ == "__main__":
    f = open("input/day1a.txt", "r").read()
    vals = f.split("\n")
    input_list = [int(i) for i in vals if len(i) > 0]
    a_soln = part_a(input_list)
    print(f"part a solution is: {a_soln}")
    b_soln = part_b(input_list)
    print(f"part b solution: {b_soln}")



