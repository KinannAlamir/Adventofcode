import os

def solve():
    input_path = os.path.join(os.path.dirname(__file__), 'Input-data')
    
    with open(input_path, 'r') as f:
        lines = f.read().splitlines()
    
    ranges = []
    ids = []
    parsing_ranges = True
    
    for line in lines:
        line = line.strip()
        if not line:
            # If we encounter a blank line and we have already parsed some ranges,
            # switch to parsing IDs.
            if parsing_ranges and ranges:
                parsing_ranges = False
            continue
            
        if parsing_ranges:
            # Ranges look like "3-5"
            if '-' in line:
                try:
                    start, end = map(int, line.split('-'))
                    ranges.append((start, end))
                except ValueError:
                    pass
        else:
            # IDs look like "1"
            try:
                ids.append(int(line))
            except ValueError:
                pass
            
    fresh_count = 0
    for ingredient_id in ids:
        for start, end in ranges:
            if start <= ingredient_id <= end:
                fresh_count += 1
                break
                
    print(f"Fresh ingredients: {fresh_count}")

if __name__ == '__main__':
    solve()
