# import strategy
import numpy as np
filename = 'input.txt'
strategy = np.loadtxt(filename, delimiter=' ', dtype=str)

# set score at 0
score = 0

# convert rock, paper, scissors moves into integers for simple comparison
comparison_dict = {"A" : 1, "B" : 2, "C" : 3, "X" : 1, "Y" : 2, "Z" : 3}

for move in strategy:
        their_move = comparison_dict.get(move[0])
        our_move = comparison_dict.get(move[1])
        if (their_move == 1 and our_move == 3) or (their_move == 2 and our_move == 1) or (their_move == 3 and our_move == 2):
            round_score = our_move + 0 #lose 
            score += round_score
        elif their_move == our_move:
            round_score = our_move + 3 #draw
            score += round_score
        else:
            round_score = our_move + 6 #win
            score += round_score

print("Part 1: " + str(score))

# reset score to 0
score = 0

# dictionary of moves
lose_dict = {"A":"Z", "B":"X", "C":"Y"}
draw_dict = {"A":"X", "B":"Y", "C":"Z"}
win_dict  = {"A":"Y", "B":"Z", "C":"X"}

for move in strategy:  
        if move[1] == "X": 
            our_move = lose_dict.get(move[0]) # get our moved based on their move
            our_move = comparison_dict.get(our_move) # get score for our move
            round_score = our_move + 0 #lose 
            score += round_score
        elif move[1] == "Y":
            our_move = draw_dict.get(move[0])
            our_move = comparison_dict.get(our_move)
            round_score = our_move + 3 #draw
            score += round_score
        else:
            our_move = win_dict.get(move[0])
            our_move = comparison_dict.get(our_move)
            round_score = our_move + 6 #win
            score += round_score

print("Part 2: " + str(score))


