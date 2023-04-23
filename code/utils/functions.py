def is_solvable(grid):
    flat_grid = grid.flatten() 
    
    inversions = 0
    for i in range(len(flat_grid)):
        for j in range(i + 1, len(flat_grid)):
            if flat_grid[j] and flat_grid[i] and flat_grid[i] > flat_grid[j]:
                inversions += 1
    return inversions % 2 == 0

def build_line(start_symb, stop_symb, sep_symb, line):
    return '\n%s%s%s\n' % (start_symb, sep_symb.join(line), stop_symb)