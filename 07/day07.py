import os
import re
from abc import ABC, abstractmethod


class Element(ABC):

    @abstractmethod
    def __init__(self, name, **kwargs):
        self.name = name
        self.parent = kwargs["parent"]
        self.size = kwargs["size"]

    @abstractmethod
    def get_name(self):
        return self.get_name

    @abstractmethod
    def get_parent(self):
        return self.parent

    def get_size(self):
        return self.size


class Folder:
    """
    :param name defines the folder name
    :param parent defines the parent folder
    """

    def __init__(self, name, **kwargs):
        self.name = name
        self.parent = kwargs["parent"]
        self.children = []
        self.size = 0

    def get_children(self):
        return self.children

    def get_child(self, name):
        if len(self.children) == 0:
            return None
        for el in self.children:
            if el.get_name() == name:
                return el
        return None

    def get_name(self):
        return self.name

    def get_size(self):
        if len(self.children) == 0:
            self.size = 0
            return 0
        self.size = 0
        for el in self.children:
            self.size += el.get_size()
        return self.size


class File(ABC):

    def __init__(self, name, **kwargs):
        """

        :param name: defines name of file
        :param kwargs:
                size    defines file size
                parent  defines parent folder
        """
        self.name = name
        self.size = kwargs["size"]
        self.parent = kwargs["parent"]

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size


class FileTree:

    def __init__(self):
        self.root = Folder("/", parent=None)
        self.cwd = self.root

    def cd(self, path: str):
        if path == "/":
            self.cwd = self.root
            return
        if path == "..":
            self.cwd = self.cwd.parent
            return
        self.cwd = self.cwd.get_child(path)

    def mkfile(self, name, size):
        new_file = File(name, size=size, parent=self.cwd)
        self.cwd.children.append(new_file)

    def dir(self, name):
        new_folder = Folder(name, parent=self.cwd)
        self.cwd.children.append(new_folder)

    def ls(self, children):
        for c in children:
            self.cwd.children.append(c)

    def find_by_size(self, max_size):
        if self.root.size < max_size:
            return self.root.size
        s = 0
        for el in self.root.children:
            s += self._find_by_size(el, max_size)
        return s

    def _find_by_size(self, el, max_size):
        if el.get_size() <= max_size:
            return el.get_size()
        if hasattr(el, "children"):
            sizes = 0
            for element in el.children:
                sizes += self._find_by_size(element, max_size)
            return sizes
        return 0


if __name__ == '__main__':
    tree = FileTree()

    print("[LOG] Start import")

    with open("./input.txt") as file:
        for line in file:
            line = line.rstrip(os.linesep)
            if re.match(r"^\$ cd .*", line):
                path = line[5:]
                tree.cd(path)
            if re.match(r"^\$ ls$", line):
                pass
            if re.match(r"^dir .*$", line):
                _name = line[4:]
                tree.dir(_name)
            if re.match(r"^[0-9]* .*$", line):
                _size, _name = re.match("([0-9]*) (.*)", line).groups()
                _size = int(_size)
                tree.mkfile(_name, _size)

    print("[LOG] Input successfuly imported")
    print("[LOG] Calculation of folder sizes started")
    tree.root.get_size()
    print("[LOG] Calculation of folder sizes completed")
    print("[LOG] Start calculation for challenge 1")
    print(tree.find_by_size(100000))
    print("[LOG] Challenge 1 computed")
