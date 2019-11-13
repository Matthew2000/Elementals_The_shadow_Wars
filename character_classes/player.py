from UniCurses import unicurses as curses

from character_classes.character import Character


class Player(Character):
    def __init__(self, name: str):
        super().__init__()

    def tick(self, input_key):
        self.update_location(input_key)

    def update_location(self, input_key):
        self.prev_location = self.location[:]
        if input_key == ord("w"):
            self.move([-1, 0])
        if input_key == ord("s"):
            self.move([1, 0])
        if input_key == ord("a"):
            self.move([0, -1])
        if input_key == ord("d"):
            self.move([0, 1])
