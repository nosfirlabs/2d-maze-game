import random

# Constants for maze dimensions
MAZE_WIDTH = 15
MAZE_HEIGHT = 15

# Create the maze as a 2D list of cells
maze = []
for i in range(MAZE_HEIGHT):
  maze.append([])
  for j in range(MAZE_WIDTH):
    # Initialize each cell with walls on all sides
    maze[i].append({"N": True, "S": True, "E": True, "W": True})

# Pick a random starting cell
current_cell = (random.randint(0, MAZE_HEIGHT-1), random.randint(0, MAZE_WIDTH-1))

# Keep track of the cells that have been visited
visited_cells = []

def visit_cell(cell):
  """Mark the given cell as visited and remove the walls to any neighboring cells that have also been visited."""
  i, j = cell
  maze[i][j]["visited"] = True
  visited_cells.append(cell)

  neighbors = []
  if i > 0:
    neighbors.append((i-1, j))
  if i < MAZE_HEIGHT-1:
    neighbors.append((i+1, j))
  if j > 0:
    neighbors.append((i, j-1))
  if j < MAZE_WIDTH-1:
    neighbors.append((i, j+1))

  for neighbor in neighbors:
    if neighbor in visited_cells:
      if neighbor[0] < i:
        maze[i][j]["N"] = False
        maze[neighbor[0]][neighbor[1]]["S"] = False
      elif neighbor[0] > i:
        maze[i][j]["S"] = False
        maze[neighbor[0]][neighbor[1]]["N"] = False
      elif neighbor[1] < j:
        maze[i][j]["W"] = False
        maze[neighbor[0]][neighbor[1]]["E"] = False
      elif neighbor[1] > j:
        maze[i][j]["E"] = False
        maze[neighbor[0]][neighbor[1]]["W"] = False

def draw_maze():
  """Print the maze to the console as a series of ASCII characters."""
  print(" _" * MAZE_WIDTH)
  for i in range(MAZE_HEIGHT):
    row = "|"
    for j in range(MAZE_WIDTH):
      if maze[i][j]["S"]:
        row += " |"
      else:
        row += "  "
    print(row)
    
def move(direction):
  """Move the player in the given direction, if possible."""
  global current_cell
  i, j = current_cell
  if direction == "N" and not maze[i][j]["N"]:
    current_cell = (i-1, j)
  elif direction == "S" and not maze[i][j]["S"]:
    current_cell = (i+1, j)
  elif direction == "E" and not maze[i][j]["E"]:
    current_cell = (i, j+1)
  elif direction == "W" and not maze[i][j]["W"]:
    current_cell = (i, j-1)
  else:
    print("Invalid move!")
    
def play_game():
  """Main function that handles the game loop."""
  # Generate the initial maze
  visit_cell(current_cell)
  draw_maze()

  # Main game loop
  while True:
    # Get player input
    move = input("Enter a direction (N, S, E, W): ").upper()

    # Update the maze and redraw it
    move(move)
    draw_maze()

    # Check if the player has won
    if current_cell == (0, 0) or current_cell == (MAZE_HEIGHT-1, MAZE_WIDTH-1):
      print("Congratulations, you won!")
      break

# Start the game
play_game()    
