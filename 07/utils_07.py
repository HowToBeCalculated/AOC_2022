from typing import Optional


class Node(object):

    def __init__(
        self,
        name: str,
        value: int = 0,
        prior: Optional["Node"] = None,
        descendants: dict[str, "Node"] = None,
    ):
        self.name = name
        self.value = value
        self.prior = prior
        if descendants == None:
            self.descendants = {}

    def __add__(self, other) -> int:
        other_value = other.value if isinstance(other, Node) else other
        return self.value + other_value

    def __radd__(self, other) -> int:
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def add_descendant(self, descendant_name: "Node", descendant_value: int = 0) -> None:
        if descendant_name not in self.descendants.keys():
            self.descendants[descendant_name] = Node(descendant_name, descendant_value, self)

    def move_to_descendant(self, descendant_name: str) -> None:
        return self.descendants[descendant_name]

    def calculate_sizes(self) -> int:
        self.value = self.value + sum([descendant.calculate_sizes() for descendant in self.descendants.values()])
        return self.value
