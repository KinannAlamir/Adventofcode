
def solve():
    try:
        with open('2025/day3/puzzleinput.md', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Input file not found.")
        return

def solve_part1(lines):
    total_joltage = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        digits = [int(c) for c in line if c.isdigit()]
        if len(digits) < 2:
            continue

        max_bank_joltage = 0
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                joltage = digits[i] * 10 + digits[j]
                if joltage > max_bank_joltage:
                    max_bank_joltage = joltage
        
        total_joltage += max_bank_joltage
    return total_joltage

def solve_part2(lines):
    total_joltage = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        digits = [int(c) for c in line if c.isdigit()]
        if len(digits) < 12:
            continue

        # Greedy approach to find the largest 12-digit subsequence
        current_idx = -1
        result_digits = []
        needed = 12
        L = len(digits)

        for k in range(needed):

            rem = needed - k
            search_end = L - rem
            search_start = current_idx + 1

            best_digit = -1
            best_digit_idx = -1
            

            for i in range(search_start, search_end + 1):
                d = digits[i]
                if d > best_digit:
                    best_digit = d
                    best_digit_idx = i
                    if d == 9:
                        break
            
            result_digits.append(best_digit)
            current_idx = best_digit_idx
        
        bank_val = 0
        for d in result_digits:
            bank_val = bank_val * 10 + d
        
        total_joltage += bank_val

    return total_joltage

def solve():
    try:
        with open('2025/day3/puzzleinput.md', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Input file not found.")
        return

    print(f"Part 1 Total output joltage: {solve_part1(lines)}")
    print(f"Part 2 Total output joltage: {solve_part2(lines)}")

if __name__ == "__main__":
    solve()
