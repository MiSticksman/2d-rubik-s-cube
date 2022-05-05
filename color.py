from enum import Enum, unique


@unique
class Color(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3
    GREEN = 4

    def __str__(self):
        return f"color: {self.name}, name: {self.value}"







