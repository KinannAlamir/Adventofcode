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
    zero_count = 0
    
    # Dial size is 100 (0-99)
    MOD = 100

    for line in lines:
        direction = line[0]
        try:
            amount = int(line[1:])
        except ValueError:
            print(f"Warning: Skipping invalid line: {line}")
            continue

        if direction == 'R':
            current_pos = (current_pos + amount) % MOD
        elif direction == 'L':
            current_pos = (current_pos - amount) % MOD
        else:
            print(f"Warning: Unknown direction in line: {line}")
            continue

        if current_pos == 0:
            zero_count += 1

    print(f"The password is: {zero_count}")

if __name__ == "__main__":
    solve()
