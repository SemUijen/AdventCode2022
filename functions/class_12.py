class Path:
    def __init__(self, id, path_matrix, input_matrix, x_pos, y_pos):
        self.id = id

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.path_matrix = path_matrix
        self.input_matrix = input_matrix

        self.shortest_path = input_matrix.shape[0] * input_matrix.shape[1]
        self.shortest_path_A = input_matrix.shape[0] * input_matrix.shape[1]

    def walk(self):
        self.path_matrix[(self.y_pos, self.x_pos)] = 1
        if self.x_pos != 0:
            if self.input_matrix[self.y_pos][self.x_pos - 1] - self.input_matrix[self.y_pos][self.x_pos] <= 1:
                self._walk(self.y_pos, self.x_pos - 1, self.path_matrix[(self.y_pos, self.x_pos)])

        if self.x_pos != self.input_matrix.shape[1] - 1:
            if self.input_matrix[self.y_pos][self.x_pos + 1] - self.input_matrix[self.y_pos][self.x_pos] <= 1:
                self._walk(self.y_pos, self.x_pos + 1, self.path_matrix[(self.y_pos, self.x_pos)])

        if self.y_pos != 0:
            if self.input_matrix[self.y_pos - 1][self.x_pos] - self.input_matrix[self.y_pos][self.x_pos] <= 1:
                self._walk(self.y_pos - 1, self.x_pos, self.path_matrix[(self.y_pos, self.x_pos)])

        if self.y_pos != self.input_matrix.shape[0] - 1:
            if self.input_matrix[self.y_pos + 1][self.x_pos] - self.input_matrix[self.y_pos][self.x_pos] <= 1:
                self._walk(self.y_pos + 1, self.x_pos, self.path_matrix[(self.y_pos, self.x_pos)])

    def _walk(self, y_pos, x_pos, previous_step):

        if self.path_matrix[y_pos][x_pos] > previous_step + 1:
            self.path_matrix[y_pos][x_pos] = previous_step + 1

            if self.input_matrix[y_pos][x_pos] != 27:

                if x_pos != 0:
                    if self.input_matrix[y_pos][x_pos - 1] - self.input_matrix[y_pos][x_pos] <= 1:
                        self._walk(y_pos, x_pos - 1, previous_step + 1)

                if x_pos != self.input_matrix.shape[1] - 1:

                    if self.input_matrix[y_pos][x_pos + 1] - self.input_matrix[y_pos][x_pos] <= 1:
                        self._walk(y_pos, x_pos + 1, previous_step + 1)

                if y_pos != 0:
                    if self.input_matrix[y_pos - 1][x_pos] - self.input_matrix[y_pos][x_pos] <= 1:
                        self._walk(y_pos - 1, x_pos, previous_step + 1)

                if y_pos != self.input_matrix.shape[0] - 1:

                    if self.input_matrix[y_pos + 1][x_pos] - self.input_matrix[y_pos][x_pos] <= 1:
                        self._walk(y_pos + 1, x_pos, previous_step + 1)


            else:

                if previous_step < self.shortest_path:
                    self.shortest_path = previous_step

    def reverese_walk(self):
        self.path_matrix[(self.y_pos, self.x_pos)] = 1
        if self.x_pos != 0:
            if self.input_matrix[self.y_pos][self.x_pos]- self.input_matrix[self.y_pos][self.x_pos - 1] <= 1:
                self._reverese_walk(self.y_pos, self.x_pos - 1, self.path_matrix[(self.y_pos, self.x_pos)])

        if self.x_pos != self.input_matrix.shape[1] - 1:
            if self.input_matrix[self.y_pos][self.x_pos] - self.input_matrix[self.y_pos][self.x_pos + 1] <= 1:
                self._reverese_walk(self.y_pos, self.x_pos + 1, self.path_matrix[(self.y_pos, self.x_pos)])

        if self.y_pos != 0:
            if self.input_matrix[self.y_pos][self.x_pos] - self.input_matrix[self.y_pos - 1][self.x_pos] <= 1:
                self._reverese_walk(self.y_pos - 1, self.x_pos, self.path_matrix[(self.y_pos, self.x_pos)])

        if self.y_pos != self.input_matrix.shape[0] - 1:
            if self.input_matrix[self.y_pos][self.x_pos] - self.input_matrix[self.y_pos + 1][self.x_pos] <= 1:
                self._reverese_walk(self.y_pos + 1, self.x_pos, self.path_matrix[(self.y_pos, self.x_pos)])

    def _reverese_walk(self, y_pos, x_pos, previous_step):

        if self.path_matrix[y_pos][x_pos] > previous_step + 1:
            self.path_matrix[y_pos][x_pos] = previous_step + 1

            if self.input_matrix[y_pos][x_pos] != 1:

                if x_pos != 0:
                    if self.input_matrix[y_pos][x_pos]- self.input_matrix[y_pos][x_pos - 1] <= 1:
                        self._reverese_walk(y_pos, x_pos - 1, previous_step + 1)

                if x_pos != self.input_matrix.shape[1] - 1:

                    if self.input_matrix[y_pos][x_pos] - self.input_matrix[y_pos][x_pos + 1] <= 1:
                        self._reverese_walk(y_pos, x_pos + 1, previous_step + 1)

                if y_pos != 0:
                    if self.input_matrix[y_pos][x_pos] - self.input_matrix[y_pos - 1][x_pos] <= 1:
                        self._reverese_walk(y_pos - 1, x_pos, previous_step + 1)

                if y_pos != self.input_matrix.shape[0] - 1:

                    if self.input_matrix[y_pos][x_pos] - self.input_matrix[y_pos + 1][x_pos] <= 1:
                        self._reverese_walk(y_pos + 1, x_pos, previous_step + 1)


            else:

                if previous_step < self.shortest_path_A:
                    self.shortest_path_A = previous_step

"""       self.path_matrix[(self.y_pos, self.x_pos)] = 1

        #allowed to walk left
        if self.x_pos != 0:
            if self.input_matrix[self.y_pos][self.x_pos - 1] - self.input_matrix[self.y_pos][self.x_pos] in [0,1]:


        # allowed to walk right
        if self.x_pos != self.input_matrix.shape[1]:

        # allowed to walk up
        if self.y_pos != 0:

        # allowed to walk down
        if self.y_pos != self.input_matrix.shape[0]:"""
