class Character:
    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.location = [0, 0]
        self.prev_location = [0, 0]
        self.name = ""
        self.symbol = "#"

    def move(self, offset: list):
        self.location[0] += offset[0]
        self.location[1] += offset[1]

    def damage(self, amount: int):
        self.health -= amount

    def heal(self, amount: int):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
