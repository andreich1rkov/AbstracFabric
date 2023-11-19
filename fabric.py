from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def createrrobotARM(self):
        pass

    @abstractmethod
    def createdecorator(self):
        pass


class SvarkaRobot():
    def create(self):
        print("Svarka robot created!")


class SborkaRobot():
    def create(self):
        print("Sborka robot created!")


class SvarkaDecorator():
    def create(self):
        print("Svarka decorator created!")


class SborkaDecorator():
    def create(self):
        print("Sborka decorator created!")


class SvarkaFactory(Factory):
    def createrrobotARM(self):
        return SvarkaRobot()

    def createdecorator(self):
        return SvarkaDecorator()


class SborkaFactory(Factory):
    def createrrobotARM(self):
        return SborkaRobot()

    def createdecorator(self):
        return SborkaDecorator()


def main(factory):
    robot = factory.createrrobotARM()
    decorator = factory.createdecorator()

    robot.create()
    decorator.create()


factory1 = SvarkaFactory()
factory2 = SborkaFactory()

main(factory1)
main(factory2)