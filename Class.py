class Hero:

    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.health = 100

    def show_hero(self):
        print('"{0}" из рассы "{1}" имеет "{2}" здоровья.'.format(self.name, self.race, self.health), end=" ")

    def health_down(self):
        self.health -= 10

    def health_up(self):
        self.health += 10

class Magic(Hero):

    def __init__(self, name, race, magiclevel):
        Hero.__init__(self, name, race)
        self.magiclevel = magiclevel

    def magic_up (self):
        self.magiclevel += 10

    def magic_down(self):
        self.magiclevel -= 10

    def show_hero(self):
        Hero.show_hero(self)
        print('Магия - "{0}"'.format(self.magiclevel))



myhero1 = Magic("Saruman", "Ork", 100)
myhero2 = Magic("Legolas", "Elf", 100)

myhero1.show_hero()
myhero2.show_hero()
print()
print("Эльф наносит удар орку")

myhero1.health_down()
myhero1.show_hero()
myhero2.magic_down()
print()
print("Орк атакует в ответ")

myhero2.health_down()
myhero2.show_hero()
myhero1.magic_down()
print()
print("Эльф находит аптечку")
myhero2.health_up()
myhero2.show_hero()
print()
myhero1.show_hero()
myhero2.show_hero()
