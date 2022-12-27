import os
import re


class Depot:
    storage: dict = {}

    def move(self, n, of, to):
        for idx in range(n):
            self.storage[to].append(self.storage[of].pop())

    def set(self, item, to):
        if to not in self.storage.keys():
            self.storage[to] = []
        self.storage[to].insert(0, item)

    def getTopCrates(self):
        result = ""
        for k, v in sorted(self.storage.items()):
            if len(v) > 0:
                result += v[-1]
        return result

    def __str__(self):
        max_length = max([len(v) for k, v in self.storage.items()])
        results = ["" for idx in range(max_length+1)]
        header = ""
        for k, v in sorted(self.storage.items()):
            header += f" {k} "
            for idx in range(max_length, 0, -1):
                if idx >= len(v):
                    results[max_length - idx] += "   "
                if idx < len(v):
                    results[max_length - idx] += f"[{v[idx]}]"
                if k != sorted(self.storage.items())[-1]:
                    results[max_length - idx] += " "
            if k != sorted(self.storage.items())[-1]:
                header += " "
        result = os.linesep.join(results)
        return result + header


class DepotDispatcher:
    _depot: Depot

    def __init__(self, depot: Depot):
        self.depot = depot

    def dispatch(self, action: str, params):
        if action == "move":
            self.depot.move(*params)


if __name__ == '__main__':
    d = Depot()
    dispatcher = DepotDispatcher(d)
    read_config = True

    with open("./input.txt") as file:
        for line in file:
            if line.rstrip(os.linesep) == "":
                read_config = False
                continue
            if read_config:
                stacks = re.findall(r".{3,4}", line)
                stacks = [s.rstrip(r"( |\n)") for s in stacks]
                for i in range(len(stacks)):
                    it = stacks[i]
                    if re.match(r"\[.\]", it):
                        it = it.lstrip("[").rstrip("]")
                        d.set(it, i+1)
                continue
            if not read_config:
                command = line.rstrip("\n").split(" ")
                dispatcher.dispatch(command[0], [int(command[1]), int(command[3]), int(command[5])])
                continue

    print(d)
    print(d.getTopCrates())
