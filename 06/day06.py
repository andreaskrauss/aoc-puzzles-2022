import os


class LiFoQueue:

    def __init__(self, max_size):
        self._queue = []
        self._max_size = max_size

    def put(self, item: chr):
        if len(self._queue) == self._max_size:
            self._queue.pop(0)
        self._queue.append(item)

    def get(self):
        if len(self._queue):
            raise IndexError("List is empty")
        return self._queue.pop(0)

    def get_unique_items(self):
        return set(self._queue)


class MarkerDetector:

    def __init__(self, buffersize):
        self._offset = 0
        self._size = buffersize
        self._has_detected = False
        self._queue = LiFoQueue(buffersize)

    def detect(self, item: chr):
        if self._has_detected:
            return
        self._queue.put(item)
        self._offset += 1
        if len(self._queue.get_unique_items()) == self._size:
            self._has_detected = True

    def get_marker(self):
        return self._offset


if __name__ == '__main__':
    packet_detector = MarkerDetector(4)
    first_msg_marker_detector = MarkerDetector(14)
    with open("./input.txt") as file:
        stream = file.readlines()[0].rstrip(os.linesep)

    for b in stream:
        packet_detector.detect(b)
        first_msg_marker_detector.detect(b)

    print(f"Challenge 1: Packet marker at index {packet_detector.get_marker()}")
    print(f"Challenge 2: Message marker at index {first_msg_marker_detector.get_marker()}")
