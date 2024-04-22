#    Main Author(s): Srushti Patel
#    Main Reviewer(s): Harsh Patel

# Function to create a deep copy of the board
def copy_board(board):
    current_board = []
    height = len(board)
    # Iterate through each row of the board
    for i in range(height):
        # Make a copy of each row and append it to the new board
        current_board.append(board[i].copy())
    return current_board

# Function to evaluate the board based on the player's perspective
def evaluate_board(board, player):
    score = 0 
    # Iterate through each cell of the board
    for row in board:
        for cell in row:
            # Update score based on the player's pieces and opponent's pieces
            if cell == player:  
                score += 1
            elif cell == -player:  
                score -= 1

    # Check for winning conditions and return infinity or negative infinity if necessary
    if all(cell == player for row in board for cell in row if cell != 0):
        return float('inf') 
    elif all(cell == -player for row in board for cell in row if cell != 0):
        return float('-inf') 
    return score 

# Function to determine all possible moves for a player on the board
def possible_moves(board, player):
    # Generate a list of all empty cells and cells occupied by the player's pieces
    moves = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 0 or board[i][j] == player]
    return moves

# Function to handle overflow after placing a piece on the board
def overflow(board, i, j, player):
    # Define the neighbors of the current cell
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    overflow_count = 4

    # Check each neighbor cell for overflow
    for x, y in neighbors:
        # Reduce the overflow count if the neighbor is outside the board or contains the player's piece
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != player:
            overflow_count -= 1
    # If the current cell's value exceeds the overflow count, distribute the excess to neighboring cells
    if abs(board[i][j]) >= overflow_count:
        board[i][j] = 0  
        for x, y in neighbors:
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                board[x][y] += player  
                if abs(board[x][y]) >= 4:  
                    overflow(board, x, y, player)

# Function to make a move on the board
def make_move(board, move, player):
    new_board = copy_board(board)
    i, j = move
    # Update the board with the player's move and handle overflow
    new_board[i][j] += player
    overflow(new_board, i, j, player)
    return new_board

# Function to check if the game is in a terminal state
def to_numeric(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return 0  # or any default value you prefer for non-numeric values

def is_terminal(board):
    player1_count = sum(to_numeric(cell) > 0 for row in board for cell in row)
    player2_count = sum(to_numeric(cell) < 0 for row in board for cell in row)

    return player1_count == 0 or player2_count == 0 or (player1_count + player2_count) == len(board) * len(board[0])

# Function to extract the move made from the original board to the new board
def extract_move(original_board, new_board):
    # Iterate through each cell of the boards and compare values to find the moved piece
    for i in range(len(original_board)):
        for j in range(len(original_board[0])):
            if original_board[i][j] != new_board[i][j]:
                return (i, j)
    return None

# Class representing the Game Tree
class GameTree:
    # Inner class representing a Node in the Game Tree
    class Node:
        def __init__(self, board, depth, player):
            self.board = board
            self.depth = depth
            self.player = player
            self.children = []
            self.score = None

    # Constructor for the Game Tree
    def __init__(self, board, player, tree_height=4):
        self.root = self.Node(board, 0, player)
        self.tree_height = tree_height
        self.build_tree(self.root, self.tree_height)

    # Method to recursively build the Game Tree
    def build_tree(self, node, height):
        if node.depth == height or is_terminal(node.board):
            
            # If the maximum depth is reached or the game is in a terminal state, evaluate the node's score
            node.score = evaluate_board(node.board, node.player)
            return

        # Generate possible moves and create child nodes for each move
        moves = possible_moves(node.board, node.player)
        for move in moves:
            new_board = make_move(node.board, move, node.player)
            child = self.Node(new_board, node.depth + 1, -node.player)
            node.children.append(child)
            self.build_tree(child, height)

    # Minimax algorithm to find the best move
    def minimax(self, node, is_maximizing):  
        if node.depth == self.tree_height or not node.children:
            # If the node is a leaf node or has no children, return its evaluated score
            return evaluate_board(node.board, node.player)

        if is_maximizing:
            # If maximizing player's turn, find the maximum score among child nodes
            value = float('-inf') 
            for child in node.children: 
                value = max(value, self.minimax(child, False))  
            return value  
        else:
            # If minimizing player's turn, find the minimum score among child nodes
            value = float('inf')  
            for child in node.children: 
                value = min(value, self.minimax(child, True))  
            return value  

    # Method to get the best move using Minimax
    def get_move(self):
        best_score = float('inf')  
        best_move = None 

        # Iterate through each child node of the root node
        for child in self.root.children:
            # Apply Minimax algorithm to find the best move
            score = self.minimax(child, False)  
            if score < best_score:
                # Update best score and move if a better move is found
                best_score = score
                best_move = extract_move(self.root.board, child.board)
        return best_move
