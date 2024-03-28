import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def calculate_heuristic(self):
        # You can implement different heuristics here.
        # For simplicity, let's use the number of misplaced tiles.
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        misplaced_tiles = sum([1 for i in range(3) for j in range(3) if self.state[i][j] != goal_state[i][j]])
        return misplaced_tiles

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(node):
    i, j = get_blank_position(node.state)
    neighbors = []

    # Possible moves: Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in moves:
        ni, nj = i + move[0], j + move[1]
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row.copy() for row in node.state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append(PuzzleNode(new_state, parent=node, action=(ni, nj), cost=node.cost + 1))

    return neighbors

def print_solution(node):
    if node is not None:
        print_solution(node.parent)
        print(f"Move {node.action}:")
        print_board(node.state)
        print()

def print_board(state):
    for row in state:
        print(row)

def a_star_search(initial_state):
    initial_node = PuzzleNode(initial_state)
    frontier = [initial_node]
    explored = set()

    while frontier:
        current_node = heapq.heappop(frontier)
        if current_node.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            print("Solution found!")
            print_solution(current_node)
            print(f"Total Cost: {current_node.cost}")
            return

        explored.add(tuple(map(tuple, current_node.state)))

        for neighbor in get_neighbors(current_node):
            if tuple(map(tuple, neighbor.state)) not in explored:
                heapq.heappush(frontier, neighbor)

    print("No solution found.")

if __name__ == "__main__":
    # Get initial state from the user
    print("Enter the initial state of the 8-Puzzle (use 0 to represent the blank space):")
    initial_state = []
    for i in range(3):
        row = list(map(int, input().split()))
        initial_state.append(row)

    a_star_search(initial_state)
