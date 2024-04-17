class Man:
    def __init__(self, level: int) -> None:
        self.level = level
        self.health_points = 100*level
        self.attack_power = 10*level
    def attack(self):
        print(f'Man attacks with {self.attack_power} strength')
    def __str__(self):
        return f'Man (level: {self.level}), hp: {self.health_points}'

man = Man(level=3)
print(man.level)
print(man.health_points)
print(man.attack_power)
man.attack()

print('-'*15)
man.level += 1
print(man.level)
print(man.health_points)
print(man.attack_power)

print('-'*15)
print(man)

class WoMan:
    def __init__(self, level: int) -> None:
        self.level = level
        self.health_points = 50*level
        self.attack_power = 15*level
    def attack(self):
        print(f'WoMan attacks with {self.attack_power} strength')
