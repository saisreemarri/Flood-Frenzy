from collections import deque


# Directions: Up, Down, Left, Right
DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


def initialize_owned(board):
    """
    Finds all cells initially connected to (0,0).

    Returns:
        owned (set): Set of (row, col) tuples.
    """

    rows = len(board)
    cols = len(board[0])

    start_color = board[0][0]

    owned = {(0, 0)}
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in DIRECTIONS:
            nx = x + dx
            ny = y + dy

            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and (nx, ny) not in owned
                and board[nx][ny] == start_color
            ):
                owned.add((nx, ny))
                queue.append((nx, ny))

    return owned


def flood_fill(board, owned, chosen_color):
    """
    Expands the player's territory after selecting a color.

    Args:
        board (list[list[int]])
        owned (set)
        chosen_color (int)

    Returns:
        updated board, updated owned set
    """

    if not owned:
        return board, owned

    # Current territory color
    r, c = next(iter(owned))
    current_color = board[r][c]

    # Ignore same-color moves
    if chosen_color == current_color:
        return board, owned

    # Recolor all owned cells
    for r, c in owned:
        board[r][c] = chosen_color

    queue = deque(owned)

    rows = len(board)
    cols = len(board[0])

    while queue:
        x, y = queue.popleft()

        for dx, dy in DIRECTIONS:
            nx = x + dx
            ny = y + dy

            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and (nx, ny) not in owned
                and board[nx][ny] == chosen_color
            ):
                owned.add((nx, ny))
                queue.append((nx, ny))

    return board, owned


def is_game_won(board, owned):
    """
    Checks if all cells are owned.
    """

    rows = len(board)
    cols = len(board[0])

    return len(owned) == rows * cols