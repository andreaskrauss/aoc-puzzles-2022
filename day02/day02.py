# A = X = Rock      = 1
# B = Y = Paper     = 2
# C = Z = Scissor   = 3
# 6 = own
# 3 = tie
# 0 = opponent
get_result = {
    "A": {
        "X": (3, 3),
        "Y": (0, 6),
        "Z": (6, 0)
    },
    "B": {
        "X": (6, 0),
        "Y": (3, 3),
        "Z": (0, 6)
    },
    "C": {
        "X": (0, 6),
        "Y": (6, 0),
        "Z": (3, 3)
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

if __name__ == '__main__':
    with open("./input.txt") as file:
        rounds = file.readlines()

for play in rounds:
    opponent, own = play.rstrip("\n").split(" ")
    result = get_result[opponent][own]
    (opponents_score, own_score) = (opponents_score + get_value(opponent) + result[0],
                                    own_score + get_value(own) + result[1])

print(opponents_score, " : ", own_score)
