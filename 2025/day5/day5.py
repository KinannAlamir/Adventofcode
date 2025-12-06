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

            if parsing_ranges and ranges:
                parsing_ranges = False
            continue
            
        if parsing_ranges:
            if '-' in line:
                try:
                    start, end = map(int, line.split('-'))
                    ranges.append((start, end))
                except ValueError:
                    pass
        else:
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
                
    print(f"Fresh ingredients (Part 1): {fresh_count}")

    # Part 2: Count total unique fresh IDs in ranges
    ranges.sort()
    merged_ranges = []
    if ranges:
        curr_start, curr_end = ranges[0]
        for i in range(1, len(ranges)):
            next_start, next_end = ranges[i]
            # Merge if overlapping or adjacent (since we are counting integers)
            # Example: 1-2 and 3-4 -> 1,2,3,4 -> 1-4. 
            # Overlap condition: next_start <= curr_end + 1
            if next_start <= curr_end + 1:
                curr_end = max(curr_end, next_end)
            else:
                merged_ranges.append((curr_start, curr_end))
                curr_start, curr_end = next_start, next_end
        merged_ranges.append((curr_start, curr_end))
        
    total_fresh_ids = sum(end - start + 1 for start, end in merged_ranges)
    print(f"Total fresh IDs (Part 2): {total_fresh_ids}")

if __name__ == '__main__':
    solve()
