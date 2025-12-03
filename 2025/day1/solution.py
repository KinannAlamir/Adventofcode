# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

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
    
    # Dial size is 100 (0-99)
    MOD = 100

    for line in lines:
        direction = line[0]
        try:
            amount = int(line[1:])
        except ValueError:
            print(f"Warning: Skipping invalid line: {line}")
            continue

        # Part 2 logic: count all zeros passed
        full_circles = amount // MOD
        part2_zeros += full_circles
        rem = amount % MOD

        if direction == 'R':
            # Check if we cross 0 in the remaining steps
            # We cross 0 if current_pos + rem >= 100
            if current_pos + rem >= MOD:
                part2_zeros += 1
            current_pos = (current_pos + amount) % MOD
        elif direction == 'L':
            # Check if we cross 0 in the remaining steps
            # We cross 0 if current_pos != 0 and rem >= current_pos
            # (If current_pos is 0, the first step goes to 99, so we don't hit 0 immediately)
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
