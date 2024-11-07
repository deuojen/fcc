# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
temp = {}


def player(prev_play, opponent_history=[]):

    global temp
    guess = "R"
    num = 6

    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)

    if len(opponent_history) > num:
        inp = "".join(opponent_history[-num:])

        if "".join(opponent_history[-(num + 1):]) in temp.keys():
            temp["".join(opponent_history[-(num + 1):])] += 1
        else:
            temp["".join(opponent_history[-(num + 1):])] = 1

        possible = [inp + "R", inp + "P", inp + "S"]

        for i in possible:
            if not i in temp.keys():
                temp[i] = 0

        predict = max(possible, key=lambda key: temp[key])

        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

        guess = ideal_response[predict[-1]]

    return guess
# import numpy as np

# # Def some functions
# def determine_reward(you, opponent): # 1: win; 0: tie; -1: loss
#   winning_situations = [['R','S'],['S','P'],['P','R']]
#   if [you, opponent] in winning_situations:
#       return 10
#   elif you == opponent:
#       return 0
#   else:
#       return -10

# def number_to_symbol(num_action):
#   if num_action == 0:
#     return 'R'
#   elif num_action == 1:
#     return 'P'
#   else:
#     return 'S'

# def symbol_to_number(sym_action):
#   if sym_action == 'R':
#     return 0
#   elif sym_action == 'P':
#     return 1
#   elif sym_action == 'S':
#     return 2

# # Initialize variables
# States = {('R', 'R'): 0,
#           ('R', 'P'): 1,
#           ('R', 'S'): 2,
#           ('P', 'R'): 3,
#           ('P', 'P'): 4,
#           ('P', 'S'): 5,
#           ('S', 'R'): 6,
#           ('S', 'P'): 7,
#           ('S', 'S'): 8}

# Q = np.zeros((9, 3))
# alpha = 0.25  #learning rate
# gamma = 0.3   #The discount factor balances the weight of future rewards in the Q-learning update.
# S = 0 #current state
# n = 1 # steps for episode (each game is considered one episode)

# # Q-Learning
# def player(prev_opponent_play, opponent_history=[]):

#   global States
#   global Q
#   global alpha
#   global gamma
#   global S
#   global A

#   opponent_history.append(prev_opponent_play)

#   if prev_opponent_play == '':
#     A = 'S'
#     return A
#   else:
#     # n, a complete game till end
#     for _ in range(n):
#       R = determine_reward(A, prev_opponent_play)
#       Sn = States[(A, prev_opponent_play)] # S_{t+1}
#       a = int(Q[Sn,:].argmax())
#       A_idx = symbol_to_number(A)

#       Q[S, A_idx] = Q[S, A_idx] + alpha*(R + gamma*Q[Sn, a] - Q[S, A_idx])

#       A = number_to_symbol(int(Q[Sn,:].argmax()))
#       S = Sn
#     return A

# steps = {}


# def player(prev_play, opponent_history=[]):
#     if prev_play != "":
#         opponent_history.append(prev_play)

#     n = 3

#     hist = opponent_history

#     guess = "R"
#     if len(hist) > n:
#         pattern = "".join(hist[-n:])

#         if "".join(hist[-(n + 1):]) in steps.keys():
#             steps["".join(hist[-(n + 1):])] += 1
#         else:
#             steps["".join(hist[-(n + 1):])] = 1

#         possible = [pattern + "R", pattern + "P", pattern + "S"]

#         for i in possible:
#             if not i in steps.keys():
#                 steps[i] = 0

#         predict = max(possible, key=lambda key: steps[key])

#         if predict[-1] == "P":
#             guess = "S"
#         if predict[-1] == "R":
#             guess = "P"
#         if predict[-1] == "S":
#             guess = "R"

#     return guess

# import random

# def player(prev_play, opponent_history=[]):
#     # Track moves and patterns
#     move_counts = {"R": 0, "P": 0, "S": 0}
#     pattern_counts = {"RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0}

#     # Append the latest move to history
#     if prev_play != '':
#         opponent_history.append(prev_play)

#     # Update move and pattern counts
#     for i in range(1, len(opponent_history)):
#         move_counts[opponent_history[i]] += 1
#         if i > 0:
#             pattern = opponent_history[i-1] + opponent_history[i]
#             if pattern in pattern_counts:
#                 pattern_counts[pattern] += 1

#     # If this is the first move, choose randomly
#     if prev_play == '':
#         return random.choice(['R', 'P', 'S'])

#     # Predict the opponent's next move based on the most frequent pattern
#     if len(opponent_history) >= 2:
#         last_move = opponent_history[-1]
#         second_last_move = opponent_history[-2]
#         pattern = second_last_move + last_move

#         if pattern in pattern_counts and pattern_counts[pattern] > 0:
#             # Choose the move that beats the predicted next move
#             predicted_move = {'R': 'P', 'P': 'S', 'S': 'R'}[last_move]
#             return predicted_move

#     # If no useful pattern found, use statistical analysis and add a level of randomness
#     if sum(move_counts.values()) == 0:
#         return random.choice(['R', 'P', 'S'])

#     # Improved strategy: Adapt based on the opponent's most recent move
#     most_common_move = max(move_counts, key=move_counts.get)
#     next_move = {'R': 'P', 'P': 'S', 'S': 'R'}[most_common_move]

#     # Add a level of randomness to avoid being too predictable
#     if random.random() < 0.2:  # 20% chance to play randomly
#         return random.choice(['R', 'P', 'S'])

#     return next_move

# def player(prev_play, opponent_history=[]):
#     opponent_history.append(prev_play)

#     guess = "R"
#     if len(opponent_history) > 2:
#         guess = opponent_history[-2]

#     return guess
