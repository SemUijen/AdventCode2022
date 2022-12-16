class Sprite:
    def __init__(self, pos_1,pos_2, pos_3):
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.pos_3 = pos_3

    def change_position(self, value):
        self.pos_1 += value
        self.pos_2 += value
        self.pos_3 += value

    def pos_list(self):
        return [self.pos_1, self.pos_2, self.pos_3]

    def reset_position(self):
        self.pos_1 = 0
        self.pos_2 = 1
        self.pos_3 = 2
