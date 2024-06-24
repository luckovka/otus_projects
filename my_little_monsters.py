class LittleMonsters:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age}"


class Children(LittleMonsters):

    def voice(self):
        return f"{self.name}: Маам..."

    def give_me(self, thing):
        return f"{self.name}: Маам... дай {thing}"

    def hunger(self):
        return f"{self.name}: Маам... сделай сэндвич с курицей"


nikola = Children('Никола', 20)
egor = Children('Егор', 11)
egor.give_me("компьютер")
nikola.give_me("денег")


class Cats(LittleMonsters):

    def voice(self):
        return f"{self.name}: Мяау..."

    def hunger(self):
        return f"{self.name}: *выразительно сидит у миски*"


klep = Cats("Клёпа", 1)
murlon = Cats("Мурлон", 17)


class ExMothersInLow(LittleMonsters):

    def voice(self, my_name, text):
        return f"{self.name}: {my_name}, {text}"


en = ExMothersInLow("Елена Николаевна", 70)
ts = ExMothersInLow("Татьяна Серафимовна", 76)


class Flowers(LittleMonsters):

    def hunger(self):
        return f"{self.name}: *выразительно сохнет*"


rose = Flowers("Минироза", 0.1)
venus = Flowers("Венерина мухоловка", 2)
kalan = Flowers("Каланхоэ", 2)


class Me:

    def __init__(self, name, status):
        self.name = name
        self.status = status


    def __str__(self):
        return f"{self.name} {self.status}"


    def lack_of_holiday(self, text):
        return f"{text}"


me = Me("Я", "мамка-забодака")


print("My little monsters are:")
print(egor)
print(nikola)
print(klep)
print(murlon)
print(en)
print(ts)
print(rose)
print(venus)
print(kalan)
print(egor.give_me("компьютер"))
print(nikola.give_me("денег"))
print(klep.voice())
print(murlon.voice())
print(egor.hunger())
print(klep.hunger())
print(murlon.hunger())
print(en.voice("Маленькая", "ах ты старая испанская галоша"))
print(ts.voice("Оленька", "в понедельник меня надо отвезти к врачу"))
print(rose.hunger())
print(venus.hunger())
print(kalan.hunger())
print(me)
print(me.lack_of_holiday("Где мой отпуск?!"))

