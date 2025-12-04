class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0
    
    def adjust_health(self, amount):
        self.health += amount
        self.health = max(self.health, 0)
