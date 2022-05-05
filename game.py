from color import Color
from states import States


class Game:

    def __init__(self):
        self.__state = States.WAITING
        self.__field = [[Color.RED for i in range(4)] for j in range(4)]
        self.__initial_of_game_field()

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def field(self):
        return self.__field

    def __initial_of_game_field(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if i % 2 == 0 and j % 2 == 0:
                    self.field[i][j] = Color.RED
                elif i % 2 == 0 and j % 2 != 0:
                    self.field[i][j] = Color.BLUE
                elif i % 2 != 0 and j % 2 != 0:
                    self.field[i][j] = Color.GREEN
                elif i % 2 != 0 and j % 2 == 0:
                    self.field[i][j] = Color.YELLOW
        self.__state = States.WAITING

    def fill_box(self, area):
        array = [[0 for i in range(2)] for j in range(2)]
        if area == 0:
            for i in range(2):
                for j in range(2):
                    array[i][j] = self.field[i][j]
        if area == 1:
            for i in range(2):
                for j in range(2):
                    array[i][j] = self.field[i][j + 2]
        if area == 2:
            for i in range(2):
                for j in range(2):
                    array[i][j] = self.field[i + 2][j]
        if area == 3:
            for i in range(2):
                for j in range(2):
                    array[i][j] = self.field[i + 2][j + 2]
        if area == 4:
            for i in range(2):
                for j in range(2):
                    array[i][j] = self.field[i + 1][j + 1]
        return array

    @staticmethod
    def rotate_box(array):
        size = len(array)
        rotate_arr = [[Color.RED for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(size):
                rotate_arr[i][j] = array[size - j - 1][i]
        return rotate_arr

    def rotate(self, area):
        box = self.rotate_box(self.fill_box(area))
        if area == 0:
            for i in range(2):
                for j in range(2):
                    self.field[i][j] = box[i][j]
        if area == 1:
            for i in range(2):
                for j in range(2):
                    self.field[i][j + 2] = box[i][j]
        if area == 2:
            for i in range(2):
                for j in range(2):
                    self.field[i + 2][j] = box[i][j]
        if area == 3:
            for i in range(2):
                for j in range(2):
                    self.field[i + 2][j + 2] = box[i][j]
        if area == 4:
            for i in range(2):
                for j in range(2):
                    self.field[i + 1][j + 1] = box[i][j]

        if self.check_win():
            print("WIN")

    def check_win(self):
        for i in range(4):
            box_after_rotate = self.fill_box(i)
            if not self.check_one_color(box_after_rotate):
                return False
        return True

    def check_one_color(self, box):
        color = box[0][0]
        for i in range(2):
            for j in range(2):
                if box[i][j] != color:
                    self.__state = States.PLAYING
                    return False
        self.__state = States.WIN
        return True

    def new_game(self):
        self.__initial_of_game_field()

    def end_game(self):
        self.__state = States.WAITING







