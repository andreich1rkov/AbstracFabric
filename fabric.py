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
    def do_ur_job(self):
        print("(started Svarka)")


class SborkaRobot():
    def create(self):
        print("Sborka robot created!")
    def do_ur_job(self):
        print("(started Sborka)")


class SvarkaDecorator():
    def create(self):
        print("Svarka decorator created!")
    def do_ur_job(self):
        print("(started decorate Svarka)")


class SborkaDecorator():
    def create(self):
        print("Sborka decorator created!")
    def do_ur_job(self):
        print("(started decorate Sborka)")

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
    robot.do_ur_job()
    print()

    decorator.create()
    decorator.do_ur_job()
    print()


factory1 = SvarkaFactory()
factory2 = SborkaFactory()

main(factory1)
main(factory2)