SOME_GLOBAL = "hai"
HOLY_SHIT = "what?"


class CoolObject:
    def __init__(self, name: str, age: int) -> None:
        self.thing = 0
        self.name = name
        self.age = age

    @staticmethod
    def static_shit(thing: str) -> None:
        print(thing)

    def say_name(self) -> None:
        print(self.name)
