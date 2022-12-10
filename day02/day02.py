# A = X = Rock      = 1
# B = Y = Paper     = 2
# C = Z = Scissor   = 3
# 6 = own
# 3 = tie
# 0 = opponent
# Result codes: x = lose, y = draw, z = win
# returns tupel of (points opponent, own points, required for result)
get_result = {
    "A": {
        "X": (3, 3, "Z"),
        "Y": (0, 6, "X"),
        "Z": (6, 0, "Y")
    },
    "B": {
        "X": (6, 0, "X"),
        "Y": (3, 3, "Y"),
        "Z": (0, 6, "Z")
    },
    "C": {
        "X": (0, 6, "Y"),
        "Y": (6, 0, "Z"),
        "Z": (3, 3, "X")
    }
}


def get_value(action: str):
    if action == "A" or action == "X":
        return 1
    if action == "B" or action == "Y":
        return 2
    if action == "C" or action == "Z":
        return 3


opponents_score = 0
own_score = 0

# Challenge 1
if __name__ == '__main__':
    with open("./input.txt") as file:
        rounds = file.readlines()

for play in rounds:
    opponent, own = play.rstrip("\n").split(" ")
    estimate = get_result[opponent][own]
    (opponents_score, own_score) = (opponents_score + get_value(opponent) + estimate[0],
                                    own_score + get_value(own) + estimate[1])

print("Challenge 1: ", opponents_score, " : ", own_score)

opponents_score = 0
own_score = 0

with open("./input.txt") as file:
    rounds = file.readlines()


for play in rounds:
    opponent, own = play.rstrip("\n").split(" ")
    estimate = get_result[opponent][own]
    result = get_result[opponent][estimate[2]]
    (opponents_score, own_score) = (opponents_score + get_value(opponent) + result[0],
                                    own_score + get_value(estimate[2]) + result[1])

print("Challenge 2: ", opponents_score, " : ", own_score)
