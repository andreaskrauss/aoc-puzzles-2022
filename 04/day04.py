class AoCRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def is_within(self, area):
        if area.start <= self.start and self.end <= area.end:
            return True
        return False

    def is_overlapping(self, area):
        self_range = range(self.start, self.end + 1)
        area_range = range(area.start, area.end + 1)
        if (self.start in area_range and self.end not in area_range) \
                or (self.start not in area_range and self.end in area_range) \
                or (area.start in self_range and area.end not in self_range) \
                or (area.start not in self_range and area.end in self_range):
            return True
        return False

    def __str__(self):
        return f"{self.start}:{self.end}"


if __name__ == '__main__':
    counter_duplicates = 0
    counter_overlaps = 0
    with open("./input.txt") as file:
        for line in file:
            area_a, area_b = [
                AoCRange(*[int(i)
                           for i
                           in ar.split("-")])
                for ar
                in line.rstrip("\n").split(",")]
            if area_a.is_within(area_b) or area_b.is_within(area_a):
                counter_duplicates += 1
                continue
            if area_a.is_overlapping(area_b):
                counter_overlaps += 1

        print(f"Challenge 1: {counter_duplicates}")
        print(f"Challenge 2: {counter_duplicates + counter_overlaps}")
