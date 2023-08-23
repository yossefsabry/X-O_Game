# ----------------------------------------------
# making x : o game using tkinter python =>
# ----------------------------------------------

# import modules
from tkinter import *
import random


def next_turn(row, col):
    """
    :param row:  for use like a grid system
    :param col: for use like a grid system,
    :return: check for the player and change the player turn
    and check if there is any win condition and stop game and change the number of player from
    players list and check for tie condition do this for the two players
    """
    global player

    # player 1
    # noinspection PyTypeChecker
    if game_btns[row][col]['text'] == "" and check_winner() == False:
        if player == players[0]:
            # noinspection PyTypeChecker
            game_btns[row][col]['text'] = player

            if not check_winner():  # check_winner() == False:
                # switch player
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner():  # check_winner == True:
                label.config(text=(players[0] + " wins!"))

            elif check_winner() == 'tie':
                label.config(text="Tie, No Winner!")

            # player 2
        elif player == players[1]:
            # noinspection PyTypeChecker
            game_btns[row][col]['text'] = player

            if not check_winner():
                # switch player
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner():
                label.config(text=(players[1] + " wins!"))

            elif check_winner() == 'tie':
                label.config(text="Draw, No Winner!")


def check_winner():
    """
    :return: the condition for win the game and tie
    """
    # check winner in row
    for row in range(3):
        # for horizontal condition
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            # change the color to green when win
            game_btns[row][0].config(text=f"{player}", bg="green")
            game_btns[row][1].config(text=f"{player}", bg="green")
            game_btns[row][2].config(text=f"{player}", bg="green")
            return True
        for col in range(3):
            if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
                game_btns[0][col].config(text=f"{player}", bg="green")
                game_btns[1][col].config(text=f"{player}", bg="green")
                game_btns[2][col].config(text=f"{player}", bg="green")
                return True

        # for diagonal's condition
        if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
            game_btns[0][0].config(text=f"{player}", bg="green")
            game_btns[1][1].config(text=f"{player}", bg="green")
            game_btns[2][2].config(text=f"{player}", bg="green")
            return True

        elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
            game_btns[0][2].config(text=f"{player}", bg="green")
            game_btns[1][1].config(text=f"{player}", bg="green")
            game_btns[2][0].config(text=f"{player}", bg="green")
            return True

        # if there are no empty spaces left
        # if there are no empty spaces left
        if not check_empty_spaces():
            for row in range(3):
                for col in range(3):
                    game_btns[row][col].config(bg="red")
            return 'tie'
        else:
            return False

def check_empty_spaces():
    """
    :return: check for the empty spaces in the Frame and return false to check_winner and check_winner return tie
    to use in next_turn
    """
    spaces = 0
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] == "":
                spaces += 1
    if spaces == 0:
        return False
    else:
        return True


def start_new_game():
    """
    :return: for the button restart to rest the game
    """
    global player
    player = random.choice(players)
    label.config(text=f"- {player} turn -")
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="#F0F0F0")


# first making the window
window = Tk()

# select the size for window
window.geometry("500x550+700+200")

# making the title for the window
window.title("X : O => game")

# making the players and chose random player
players = ["x", "o"]
player = random.choice(players)

# making the window 3D for Frame
game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# making label for the turn player
label = Label(text=f"- {player} turn -", font=("system", 40))
label.pack()

# making restart button
btn_restart = Button(text="Restart", font=("system", 20), command=start_new_game)
btn_restart.pack(side='top')

# making the btns frames for the window
btns_frames = Frame(window)
btns_frames.pack()
for row in range(3):
    for col in range(3):
        # noinspection PyTypeChecker
        game_btns[row][col] = Button(btns_frames, text="", font=("system", 40), width=4, height=2,
                                     # use lambda because the command don't take function with attributes'
                                     # example next_turn(col ,row) so we should get to the next_turn an
                                     # arguments, so I use lambda
                                     command=lambda row=row, col=col: next_turn(row, col))

        # show the btns in grid system
        game_btns[row][col].grid(row=row, column=col)

    # making loop the make the work until the quit
window.mainloop()
