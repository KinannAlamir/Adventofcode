def solve():
    """
    Solves the Day 4 Part 2 problem.
    
    Reads the grid from 'input.txt', then iteratively removes rolls of paper ('@')
    that have fewer than 4 neighbors (also '@').
    """
    with open("input.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    rows = len(grid)
    total_removed = 0

    while True:
        to_remove = []
        for r in range(rows):
            cols = len(grid[r])
            for c in range(cols):
                if grid[r][c] == '@':
                    neighbor_count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
                                if grid[nr][nc] == '@':
                                    neighbor_count += 1
                    
                    if neighbor_count < 4:
                        to_remove.append((r, c))
        
        if not to_remove:
            break
        
        total_removed += len(to_remove)
        
        for r, c in to_remove:
            grid[r][c] = '.'

    print(f"Total removed rolls: {total_removed}")

if __name__ == "__main__":
    solve()
