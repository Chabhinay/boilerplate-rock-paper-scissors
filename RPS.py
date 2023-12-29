# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import numpy as np

ideal_response = {"P": "S", "R": "P", "S": "R"}
my_moves = ["R"]
opponent_history = []
stgy = [0, 0, 0, 0]
og = ["", "", "", ""]
sg = ["", "", "", ""]
opponent_play_order = {}
my_play_order = {}

def player(prev_play):
   if prev_play in ["R", "P", "S"]:
       opponent_history.append(prev_play)
       for i in range(0, 4):
           if og[i] == prev_play:
               stgy[i] += 1
   else:
       reset()

   my_last_ten = my_moves[-10:]
   if len(my_last_ten) > 0:
       my_most_frequent_move = max(set(my_last_ten), key=my_last_ten.count)
       og[0] = ideal_response[my_most_frequent_move]
       sg[0] = ideal_response[og[0]]

   if len(my_moves) > 0:
       my_last_play = my_moves[-1]
       og[1] = ideal_response[my_last_play]
       sg[1] = ideal_response[og[1]]

   if len(opponent_history) >= 3:
       og[2] = predict_move(opponent_history, 3, opponent_play_order)
       sg[2] = ideal_response[og[2]]

   if len(my_moves) >= 2:
       og[3] = ideal_response[predict_move(my_moves, 2, my_play_order)]
       sg[3] = ideal_response[og[3]]

   best_stgy = np.argmax(stgy)
   guess = sg[best_stgy]
   if guess == "":
       guess = "S"
   my_moves.append(guess)
   return guess

def predict_move(history, n, play_order):
   if "".join(history[-n:]) in play_order.keys():
       play_order["".join(history[-n:])] += 1
   else:
       play_order["".join(history[-n:])] = 1
   possible = ["".join(history[-(n - 1):]) + k for k in ["R", "P", "S"]]
   for pm in possible:
       if not pm in play_order.keys():
           play_order[pm] = 0
   predict = max(possible, key=lambda key: play_order[key])
   return predict[-1]

def reset():
   global my_moves, opponent_history, stgy, og, sg, opponent_play_order, my_play_order
   my_moves = ["R"]
   opponent_history.clear()
   stgy = [0, 0, 0, 0]
   og = ["", "", "", ""]
   sg = ["", "", "", ""]
   opponent_play_order = {}
   my_play_order = {}
