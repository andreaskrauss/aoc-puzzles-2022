if __name__ == '__main__':
    with open("./input.txt") as file:
        logs = file.readlines()

    book = []
    calories = 0
    for log in logs:
        log = log.rstrip("\n")
        if log == '':
            book.append(calories)
            calories = 0
            continue
        else:
            calories += int(log)
    # Day 1 - Star 1
    print(max(book))
    # Day 1 - Star 2
    book.sort(reverse=True)
    print(sum(book[0:3]))

