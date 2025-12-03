import os

def is_invalid(n: int) -> bool:
    s = str(n)
    length = len(s)
    for unit_len in range(1, length // 2 + 1):
        if length % unit_len == 0:
            unit = s[:unit_len]
            repeats = length // unit_len
            if unit * repeats == s:
                return True
    return False


def solve():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "puzzleinput.md")
    
    with open(input_path, "r") as f:
        content = f.read()
    
    lines = content.strip().splitlines()
    data_line = ""
    for line in lines:
        if line.strip().startswith("```"):
            continue
        if "," in line or "-" in line:
            data_line = line.strip()
            break
            
    if not data_line:
        print("Could not find input data")
        return

    ranges = data_line.split(",")
    total_invalid_sum = 0
    
    for r in ranges:
        start_str, end_str = r.split("-")
        start = int(start_str)
        end = int(end_str)
        
        for n in range(start, end + 1):
            if is_invalid(n):
                total_invalid_sum += n
                
    print(f"Total sum of invalid IDs: {total_invalid_sum}")


if __name__ == "__main__":
    solve()
