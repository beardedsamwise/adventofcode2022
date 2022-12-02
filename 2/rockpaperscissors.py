# import strategy
import numpy as np
filename = 'input.txt'
strategy = np.loadtxt(filename, delimiter=' ', skiprows=1, dtype=str)

# set score at 0
score = 0

# convert rock, paper, scissors moves into integers for simple comparison
win_dict = {"A" : 1, "B" : 2, "C" : 3, "X" : 1, "Y" : 2, "Z" : 3}

def get_move(move):
    if move == "X":
        value = win_dict.get("X")
    elif move == "Y":
        value = win_dict.get("Y")
    elif move == "Z":
        value = win_dict.get("Z")     
    elif move == "A":
        value = win_dict.get("A")
    elif move == "B":
        value = win_dict.get("B")   
    else:
        value = win_dict.get("C")
    return value


for move in strategy:
        their_move = get_move(move[0])
        our_move = get_move(move[1])
        if their_move > our_move:
            round_score = our_move + 0 #lose 
            print(str(round_score) + " lose " + str(our_move))
            score += round_score
        elif their_move < our_move:
            round_score = our_move + 6 #win
            print(str(round_score) + " win " + str(our_move))
            score += round_score
        elif their_move == our_move:
            round_score = our_move + 3 #draw
            print(str(round_score) + " draw " + str(our_move))
            score += round_score

print(score)



