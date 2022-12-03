# import strategy
import numpy as np
filename = 'input.txt'
strategy = np.loadtxt(filename, delimiter=' ', dtype=str)

# set score at 0
score = 0

# convert rock, paper, scissors moves into integers for simple comparison
win_dict = {"A" : 1, "B" : 2, "C" : 3, "X" : 1, "Y" : 2, "Z" : 3}


for move in strategy:
        their_move = win_dict.get(move[0])
        our_move = win_dict.get(move[1])
        # their winning moves - rock beatss scissors + paper beats rock + scissors beats paper
        if (their_move == 1 and our_move == 3) or (their_move == 2 and our_move == 1) or (their_move == 3 and our_move == 2):
            round_score = our_move + 0 #lose 
            score += round_score
        # draw
        elif their_move == our_move:
            round_score = our_move + 3 #draw
            score += round_score
        # otherwise we win
        else:
            round_score = our_move + 6 #win
            score += round_score


print(score)



