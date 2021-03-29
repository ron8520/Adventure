class Adventurer:
    def __init__(self):
        self.skill = 5
        self.will = 5
        self.inventory = []
    def get_inv(self):
        """TODO: Returns the adventurer's inventory."""
        return self.inventory

    def get_skill(self):
        """TODO: Returns the adventurer's skill level. Whether this value is generated before or after item bonuses are applied is your decision to make."""
        return self.skill

    def get_will(self):
        """TODO: Returns the adventurer's will power. Whether this value is generated before or after item bonuses are applied is your decision to make."""
        return self.will

    def take(self, item):
        """TODO: Adds an item to the adventurer's inventory."""
        self.inventory.append(item)

    def check_self(self):
        """TODO: Shows adventurer stats and all item stats."""
        print(self.skill)
        print(self.will)
        print(self.inventory)
