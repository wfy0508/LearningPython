class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("Animal run")


class Dog(Animal):

    def run(self):
        print("Dog run")
        super().run()


dog = Dog("wangcai")
dog.run()
