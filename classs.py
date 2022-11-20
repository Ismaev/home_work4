class Hero:
    def __init__(self, name , ability = True):
        self.name = name
        self.ability = ability
class Hero_super(Hero):
    def __str__(self):
        self.name = str
    def hero(self):
        print(f'{self.name} it is super_Hero')

