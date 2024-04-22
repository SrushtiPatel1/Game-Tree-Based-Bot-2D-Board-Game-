def get_overflow_list(new_grid):
    rows = len(new_grid)
    cols = len(new_grid[0])
    overflowing_cells = []

    for r in range(rows):
        for c in range(cols):
            if isinstance(new_grid[r][c], (int, float)):
                surrounding = sum(1 for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)] if 0 <= r + dr < rows and 0 <= c + dc < cols)

                if abs(new_grid[r][c]) >= surrounding:
                    overflowing_cells.append((r, c))

    return overflowing_cells if overflowing_cells else None



def overflow(new_grid, a_queue):
    def spread_overflow(r, c, is_negative):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(new_grid) and 0 <= nc < len(new_grid[0]):
                if is_negative:
                    new_grid[nr][nc] = -(abs(new_grid[nr][nc]) + 1)
                else:
                    new_grid[nr][nc] = abs(new_grid[nr][nc]) + 1

    overflow_list = get_overflow_list(new_grid)
    
    if all(x <= 0 for row in new_grid for x in row):
        return 0

    if all(x >= 0 for row in new_grid for x in row):
        return 0

    if not overflow_list:
        return 0

    is_negative = new_grid[overflow_list[0][0]][overflow_list[0][1]] < 0

    for r, c in overflow_list:
        new_grid[r][c] = 0

    for r, c in overflow_list:
        spread_overflow(r, c, is_negative)

    a_queue.enqueue([row[:] for row in new_grid])
    
    return 1 + overflow(new_grid, a_queue)