import turtle
from random import randint
from time import sleep

# initialise empty 9 by 9 grid
#grid = []
#grid.append([3, 0, 6, 5, 0, 8, 4, 0, 0])
#grid.append([5, 2, 0, 0, 0, 0, 0, 0, 0])
#grid.append([0, 8, 7, 0, 0, 0, 0, 3, 1])
#grid.append([0, 0, 3, 0, 1, 0, 0, 8, 0])
#grid.append([9, 0, 0, 8, 6, 3, 0, 0, 5])
#grid.append([0, 5, 0, 0, 9, 0, 6, 0, 0])
#grid.append([1, 3, 0, 0, 0, 0, 2, 5, 0])
#grid.append([0, 0, 0, 0, 0, 0, 0, 7, 4])
#grid.append([0, 0, 5, 2, 0, 6, 3, 0, 0])

grid = []
grid.append([1, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

#def print_grid(grid):
#    for i in range(0, 9):
#        for j in range(0, 9):
#            print(grid[i][j], end='\t')
#        print()

def print_grid(grid):
    #print grid using function I took from online
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

def is_safe(grid_safe, position, n):
    #read in the coordinates for the position of proposed number "n"
    x = position[0]
    y = position[1]
    #set up original position so we can revert the graph
    original = grid_safe[x][y]
    #change number on the grid to be the proposed number "n"
    grid_safe[x][y] = n
    # set up hash map for rows and cols
    grid_row = [0] * 9
    grid_col = [0] * 9
    # check if rows are safe
    for i in range(0, 9):
        for j in range(0, 9):
            current_num = grid_safe[i][j]
            if current_num != 0:
                grid_row[current_num - 1] += 1
                if grid_row[current_num - 1] > 1:
                    #reset grid
                    grid_safe[x][y] = original
                    return False
                    # return False
        # print("this is grid row before reset", grid_row)
        grid_row = [0] * 9

    # check if the columns are safe
    for i in range(0, 9):
        for j in range(0, 9):
            current_num = grid_safe[j][i]
            if current_num != 0:
                grid_col[current_num - 1] += 1
                if grid_col[current_num - 1] > 1:
                    # reset grid
                    grid_safe[x][y] = original
                    return False
        # print("this is grid col before reset", grid_col)
        grid_col = [0] * 9

    # check if 3x3 boxes are safe
    box_rows = position[0] // 3
    box_cols = position[1] // 3

    for i in range(box_rows * 3, box_rows * 3 + 3):
        for j in range(box_cols * 3, box_cols * 3 + 3):
            if grid_safe[i][j] == n and (i, j) != position:
                # reset grid
                grid_safe[x][y] = original
                return False
    grid_safe[x][y] = original
    return True


def solve(grid):
    #solve the board using backtracking
    #check to see if there are any empty spaces
    empty_space = find_empty(grid)
    #if there are no empty spaces on the board then we are done and can exit
    if empty_space == False:
        return True
    #otherwise, assign the empty space tuple to some variables
    else:
        (row, col) = empty_space

    #for the empty space plug in all possible safe numbers from 1-10
    for i in range(1, 10):
        if is_safe(grid, (row, col), i):
            #if it is safe set that location on the grid equal to i
            grid[row][col] = i

            if solve(grid) == True:
                return True

            #the space was invalid and we need to reset it
            grid[row][col] = 0

    return False



def find_empty(grid):
    # check if the space is empty or not
    for i in range(0, 9):
        for j in range(0, 9):
            # if it is empty then return the coordinates
            if grid[i][j] == 0:
                return (i, j)
    #no empty spots so we return false
    return False


if solve(grid):
    print_grid(grid)
else:
    print("No solution exists")

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")
myPen.hideturtle()
topLeft_x = -150
topLeft_y = 150


def text(message, x, y, size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x, y)
    myPen.write(message, align="left", font=FONT)


# A procedure to draw the grid on screen using Python Turtle
def drawGrid(grid):
    intDim = 35
    for row in range(0, 10):
        if (row % 3) == 0:
            myPen.pensize(3)
        else:
            myPen.pensize(1)
        myPen.penup()
        myPen.goto(topLeft_x, topLeft_y - row * intDim)
        myPen.pendown()
        myPen.goto(topLeft_x + 9 * intDim, topLeft_y - row * intDim)
    for col in range(0, 10):
        if (col % 3) == 0:
            myPen.pensize(3)
        else:
            myPen.pensize(1)
        myPen.penup()
        myPen.goto(topLeft_x + col * intDim, topLeft_y)
        myPen.pendown()
        myPen.goto(topLeft_x + col * intDim, topLeft_y - 9 * intDim)

    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] != 0:
                text(grid[row][col], topLeft_x + col * intDim + 9, topLeft_y - row * intDim - intDim + 8, 18)
    turtle.done()

if solve(grid):
    drawGrid(grid)

# drawGrid(grid)


