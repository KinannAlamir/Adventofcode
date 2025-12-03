import pathlib

def solve():
    input_path = pathlib.Path(__file__).parent / "puzzleinput.md"
    
    if not input_path.exists():
        print(f"Error: Input file not found at {input_path}")
        return

    with open(input_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    current_pos = 50
    part1_zeros = 0
    part2_zeros = 0
    
    MOD = 100

    for line in lines:
        direction = line[0]
        try:
            amount = int(line[1:])
        except ValueError:
            print(f"Warning: Skipping invalid line: {line}")
            continue

        full_circles = amount // MOD
        part2_zeros += full_circles
        rem = amount % MOD

        if direction == 'R':

            if current_pos + rem >= MOD:
                part2_zeros += 1
            current_pos = (current_pos + amount) % MOD
        elif direction == 'L':

            if current_pos != 0 and rem >= current_pos:
                part2_zeros += 1
            current_pos = (current_pos - amount) % MOD
        else:
            print(f"Warning: Unknown direction in line: {line}")
            continue

        if current_pos == 0:
            part1_zeros += 1

    print(f"Part 1 password: {part1_zeros}")
    print(f"Part 2 password: {part2_zeros}")

if __name__ == "__main__":
    solve()
