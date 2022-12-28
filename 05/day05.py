import os
import re


class Depot:

    def __init__(self):
        self.storage: dict = {}

    def do(self, move, params):
        move(self.storage, params[0], params[1], params[2])

    def set(self, item, to):
        if to not in self.storage.keys():
            self.storage[to] = []
        self.storage[to].insert(0, item)

    def get_top_crates(self):
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


class CrateMover9000:
    _depot: Depot

    def __init__(self, depot: Depot):
        self._depot = depot

    def dispatch(self, action: str, params):
        if action == "move":
            n, of, to = params
            for idx in range(n):
                self._depot.storage[to].append(self._depot.storage[of].pop())



class CrateMover9001:
    _depot: Depot

    def __init__(self, depot: Depot):
        self._depot = depot

    def dispatch(self, action: str, params):
        if action == "move":
            n, of, to = params
            self._depot.storage[to].extend(self._depot.storage[of][-n:])
            self._depot.storage[of] = self._depot.storage[of][0:-n]


if __name__ == '__main__':
    d1 = Depot()
    mover1 = CrateMover9000(d1)
    d2 = Depot()
    mover2 = CrateMover9001(d2)

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
                        d1.set(it, i + 1)
                        d2.set(it, i + 1)
                continue
            if not read_config:
                command = line.rstrip("\n").split(" ")
                mover1.dispatch(command[0], [int(command[1]), int(command[3]), int(command[5])])
                mover2.dispatch(command[0], [int(command[1]), int(command[3]), int(command[5])])
                continue

    print(d1)
    print(d2)
    print(f"{os.linesep}=== Requested Outputs ===")
    print(f"Challenge 1: {d1.get_top_crates()}")
    print(f"Challenge 2: {d2.get_top_crates()}")
