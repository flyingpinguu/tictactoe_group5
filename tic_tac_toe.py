# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
grid=[[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
print("Welcome to a new round of Tic-Tac-Toe!")
turn = 1
def check_space(line,column):
    if grid[line][column] == " ":
        return True
    else:
        return False
def printboard():
    for line in grid:
        print(line)
def userinput(symbol):
    line = int(input("Write the number of the line you want to place your symbol: "))
    column = int(input("Write the number of the column you want to place: "))
    line -= 1
    column -= 1
    if check_space(line,column) == False:
        return False
    grid[line][column]=symbol
    return True
def checkwin():

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != " ": #diagonal 1
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[1][1] != " ": # check for diagnol 2
        return True
    for i in range(len(grid)):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != " ": # check rows
            return True
    for j in range(len(grid)):
        if grid[0][j] == grid[1][j] == grid[2][j] and grid[0][j] != " ": # check columns
            return True

while True:
    players = ["x", "o"]
    active_symbol = players[turn%2]
    if userinput(active_symbol) == False:
        print("That didn't work enter new space")
        continue
    if checkwin() == True:
        print("Congrats you won!")
        printboard()
        if input("Would you like to play again? Type 'yes'. Otherwise type 'quit': ") == "yes":
            turn = 1
            continue
        break
    printboard()
    if turn >= 9:
        print("Tie!")
        if input("Would you like to play again? Type 'yes'. Otherwise type 'quit': ") == "yes":
            turn = 1
            continue
        break
    turn += 1




# Tic-tac-toe game
if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
    print("this is the end")
