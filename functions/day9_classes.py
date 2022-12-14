class Head:
    def __init__(self, x_pos, y_pos, tail):
        self.x_pos= x_pos
        self.y_pos = y_pos
        self.tail = tail

    def move(self, direction, steps):

        for step in range(steps):

            if direction == "R":
                self._move(1, 'x')
            if direction == 'L':
                self._move(-1, 'x')

            if direction == "U":
                self._move(1, 'y')
            if direction == 'D':
                self._move(-1, 'y')

    def _move(self, step, axis):

        if axis == 'y':
            old_y = self.y_pos
            new_y = self.y_pos + step

            if abs(new_y - self.tail.y_pos) > 1 or abs(self.x_pos - self.tail.x_pos) > 1:
                self.tail.move(self.x_pos, old_y)

            self.y_pos = new_y

        if axis == 'x':
            old_x = self.x_pos
            new_x = self.x_pos + step

            if abs(self.y_pos - self.tail.y_pos) > 1 or abs(new_x - self.tail.x_pos) > 1:
                self.tail.move(old_x, self.y_pos)

            self.x_pos = new_x

class Tail:
    def __init__(self, x_pos, y_pos, matrix, tail):
        self.x_pos= x_pos
        self.y_pos = y_pos
        self.matrix = matrix

        self.tail = tail
    def move(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.add_trace()

    def add_trace(self):

        if self.matrix[(self.y_pos, self.x_pos)] == 0:
            self.matrix[(self.y_pos, self.x_pos)] = 1
