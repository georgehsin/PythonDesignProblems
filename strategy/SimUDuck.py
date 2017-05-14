# Duck Simulator using Strategy Design Pattern

class Duck:
    def __init__(self):
    	self.flyBehavior = None
    	self.quackBehavior = None

    def display(self):
        pass

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()

    def setQuackBehavior(self, quackBehavior):
        self.quackBehavior = quackBehavior

    def setFlyBehavior(self, flyBehavior):
        self.flyBehavior = flyBehavior


# <---------------------------------------------->
# <-------- Encapsulated Quack Behaviors -------->
# <---------------------------------------------->

class QuackBehavior:
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class FakeQuack(QuackBehavior):
    def quack(self):
        print("Quack")

# <---------------------------------------------->
# <--------- Encapsulated Fly Behaviors --------->
# <---------------------------------------------->

class FlyBehavior():
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


# <---------------------------------------------->
# <--------------- Duck Classes ----------------->
# <---------------------------------------------->


class MallardDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyWithWings()
        self.quackBehavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")


class RubberDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = Squeak()

    def display(self):
        print("I'm a rubber duckie")

class ModelDuck(Duck):
    def __init__(self):
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = Quack()

    def display(self):
        print("I'm a model duck")


if __name__ == '__main__':
    mallard = MallardDuck()
    mallard.performQuack()
    mallard.performFly()

    model = ModelDuck()
    model.performFly()
    model.setFlyBehavior(FlyRocketPowered())
    model.performFly()