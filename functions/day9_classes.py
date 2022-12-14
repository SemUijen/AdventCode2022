class Head:
    def __init__(self, x_pos, y_pos, tail):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.tail = tail

    def move(self, direction, steps):

        for step in range(steps):

            if direction == "R":
                self._move(1, 'x')
            if direction == 'L':
                self._move(-1, 'x')

            if direction == "U":
                self._move(-1, 'y')
            if direction == 'D':
                self._move(1, 'y')

    def _move(self, step, axis):

        if axis == 'y':
            old_y = self.y_pos
            new_y = self.y_pos + step

            if abs(new_y - self.tail.y_pos) > 1 or abs(self.x_pos - self.tail.x_pos) > 1:
                self.tail.move(self.x_pos, old_y, axis, step)

            self.y_pos = new_y

        if axis == 'x':
            old_x = self.x_pos
            new_x = self.x_pos + step

            if abs(self.y_pos - self.tail.y_pos) > 1 or abs(new_x - self.tail.x_pos) > 1:
                self.tail.move(old_x, self.y_pos, axis, step)

            self.x_pos = new_x

    def find_tail(self):
        if self.tail is not None:
            return self._find_tail(self.tail)

        return self

    def _find_tail(self, Tail):

        if Tail.tail is not None:
            Tail = self._find_tail(Tail.tail)

        return Tail


class Tail:
    def __init__(self, id, x_pos, y_pos, matrix, tail):
        self.id = id
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.matrix = matrix

        self.tail = tail

    def move(self, x_pos, y_pos, axis, step):

        if self.tail is not None:

            self._move(x_pos, y_pos, step, axis)

        else:
            print(self.id)
            print(self.x_pos, self.y_pos)
            print(x_pos, y_pos)
            self.x_pos = x_pos
            self.y_pos = y_pos
            self.add_trace()

    def add_trace(self):
        if self.matrix[(self.y_pos, self.x_pos)] == 0:
            self.matrix[(self.y_pos, self.x_pos)] = 1

    def _move(self, x_pos, y_pos, step, axis):

        self.x_pos = x_pos
        self.y_pos = y_pos

        if abs(self.y_pos - self.tail.y_pos) > 1 or abs(self.x_pos - self.tail.x_pos) > 1:

            if self.y_pos != self.tail.y_pos and self.x_pos != self.tail.x_pos:
                #print(self.id, self.tail.id)
                #print(self.x_pos, self.tail.x_pos, self.y_pos, self.tail.y_pos)

                if self.x_pos - self.tail.x_pos < 0 and self.y_pos - self.tail.y_pos < 0:
                    self.tail.move(self.tail.x_pos - 1, self.tail.y_pos - 1, axis, step)

                if self.x_pos - self.tail.x_pos > 0 and self.y_pos - self.tail.y_pos < 0:
                    self.tail.move(self.tail.x_pos + 1, self.tail.y_pos - 1, axis, step)

                if self.x_pos - self.tail.x_pos < 0 and self.y_pos - self.tail.y_pos > 0:
                    self.tail.move(self.tail.x_pos - 1, self.tail.y_pos + 1, axis, step)

                if self.x_pos - self.tail.x_pos > 0 and self.y_pos - self.tail.y_pos > 0:
                    self.tail.move(self.tail.x_pos + 1, self.tail.y_pos + 1, axis, step)

            else:
                if axis == 'y':
                    self.tail.move(self.tail.x_pos, self.tail.y_pos + step, axis, step)

                if axis == 'x':
                    self.tail.move(self.tail.x_pos + step, self.tail.y_pos, axis, step)
