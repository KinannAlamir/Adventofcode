import os

def solve():
    input_path = os.path.join(os.path.dirname(__file__), 'inputdata.md')
    
    with open(input_path, 'r') as f:
        lines = f.read().splitlines()
    
    # Remove empty lines at the end if any
    while lines and not lines[-1].strip():
        lines.pop()
        
    if not lines:
        return

    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]
    
    # Identify empty columns
    empty_cols = []
    for col in range(max_len):
        is_empty = True
        for line in padded_lines:
            if line[col] != ' ':
                is_empty = False
                break
        if is_empty:
            empty_cols.append(col)
            
    blocks = []
    start_col = 0
    split_points = empty_cols + [max_len]
    
    for split_col in split_points:
        if split_col > start_col:
            block_lines = []
            for line in padded_lines:
                block_lines.append(line[start_col:split_col])
            
            if any(line.strip() for line in block_lines):
                blocks.append(block_lines)
        
        start_col = split_col + 1
        
    grand_total = 0
    
    for block in blocks:
        operator_row = block[-1].strip()
        if not operator_row:

            operator = None
            for i in range(len(block) - 1, -1, -1):
                row_content = block[i].strip()
                if row_content in ('+', '*'):
                    operator = row_content
                    numbers_rows = block[:i]
                    break
            if operator is None:
                continue
        else:
            operator = operator_row
            numbers_rows = block[:-1]
            
        numbers = []
        for row in numbers_rows:
            s = row.strip()
            if s:
                try:
                    numbers.append(int(s))
                except ValueError:
                    pass
                    
        if not numbers:
            continue
            
        result = numbers[0]
        for num in numbers[1:]:
            if operator == '+':
                result += num
            elif operator == '*':
                result *= num
                
        grand_total += result
        
    print(f"Grand total (Part 1): {grand_total}")

    # Part 2
    grand_total_part2 = 0
    for block in blocks:
        # Find operator row (same logic as Part 1)
        operator_row_idx = -1
        operator = None
        
        # Check last row first
        if block[-1].strip() in ('+', '*'):
            operator = block[-1].strip()
            operator_row_idx = len(block) - 1
        else:
            # Search upwards
            for i in range(len(block) - 1, -1, -1):
                row_content = block[i].strip()
                if row_content in ('+', '*'):
                    operator = row_content
                    operator_row_idx = i
                    break
        
        if operator is None:
            continue
            
        numbers_rows = block[:operator_row_idx]
        if not numbers_rows:
            continue
            
        # Parse numbers column by column
        numbers = []
        width = len(numbers_rows[0])
        
        # Iterate columns (order doesn't matter for +/*, but problem says right-to-left)
        for col in range(width - 1, -1, -1):
            digits = []
            for row in numbers_rows:
                char = row[col]
                if char.isdigit():
                    digits.append(char)
            
            if digits:
                numbers.append(int("".join(digits)))
                
        if not numbers:
            continue
            
        result = numbers[0]
        for num in numbers[1:]:
            if operator == '+':
                result += num
            elif operator == '*':
                result *= num
                
        grand_total_part2 += result

    print(f"Grand total (Part 2): {grand_total_part2}")

if __name__ == '__main__':
    solve()
