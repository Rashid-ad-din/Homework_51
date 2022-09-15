from random import randint

from django.core.handlers.wsgi import WSGIRequest

from webapp.db import DB


class Cat:
    def __init__(self, name: str, age: int, happiness: int = 50, satiety: int = 50):
        self.name = name
        self.age = age
        self.happiness = happiness
        self.satiety = satiety
        self.state = None

    @classmethod
    def age_fun(cls):
        return randint(1, 20)

    @staticmethod
    def add_cat(request: WSGIRequest):
        DB.cat = Cat(request.POST.get('cat'), Cat.age_fun())

    def state_fun(self):

        if self.state != 'sleep':
            if self.happiness >= 40 and self.satiety <= 100 and self.satiety != 0:
                self.state = 'happy'
                return "Cat is happy!"
            elif self.happiness in range(1, 40) and self.satiety <= 100 and self.satiety != 0:
                self.state = 'sad'
                return "Cat is sad!"
            elif self.happiness <= 0 and self.satiety <= 0:
                self.happiness = 0
                self.satiety = 0
                self.state = 'hungry'
                return "Cat is hungry!"
            elif self.happiness <= 0:
                self.happiness = 0
                self.state = 'fury'
                return "Cat is angry!"
            elif self.satiety > 100 and self.happiness > 0:
                self.state = 'overfed'
                return "Cat is overfed!"
            elif self.satiety <= 0:
                self.satiety = 0
                self.state = 'hungry'
                return "Cat is hungry!"
        elif self.state == 'sleep':
            return "Cat is sleeping!"

    def set_state(self, state):
        self.state = state

    def play(self):
        if self.satiety <= 0:
            self.state_fun()
            return
        x = randint(1, 3)
        if x == 1:
            self.happiness = 0
            self.satiety -= 10
        elif self.state == 'sleep':
            self.happiness -= 5
            self.satiety -= 10
        else:
            self.happiness += 15
            self.satiety -= 10
        self.set_state(None)
        self.state_fun()

    def sleep(self):
        self.happiness += 15
        self.satiety -= 10

    def eat(self):
        self.happiness += 5
        self.satiety += 15
        if self.satiety > 100:
            self.happiness -= 30
