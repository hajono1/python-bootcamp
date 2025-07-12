from abc import ABC, abstractmethod

class Character(ABC):
    """Template or guideline for specific characters"""

    def __init__(self, health=10, defense=10):
        self.health = health
        self.defense = defense

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()

#SUB HIERARCHY
class Knight(Character):
    """Special Character focusing on defense"""

    def attack(self, other):
        damage = self.defense - other.defense
        other.health -= damage

class Mage(Character):
    def __init__(self, health=10, defense=5, magic = 20):
        super().__init__(health, defense)
        self.magic = magic
    def attack(self, other):
        damage = self.magic - other.defense
        other.health -= damage

class Warrior(Character):
    def __init__(self, health=5, defense=10, attack = 20):
        super().__init__(health, defense)
        self.attack = attack
    def attack(self, other):
        damage = self.attack - other.defense
        other.health -= damage


mage1 = Mage()
warrior1 = Warrior()

mage1.attack(warrior1)