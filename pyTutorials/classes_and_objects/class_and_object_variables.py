class Robot:
    """Represents s robot with a name"""

    # A class variable, counting the number of robots
    population = 0
    
    def __init__(self,name):
        """Initializes the Data"""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this initialization is done, we create one robot
        Robot.population += 1

    def die(self):
        """Robot Dying"""
        print("{} is being Destroyed".format(self.name))

        # When a robot dies, the population is reduced
        Robot.population -= 1

        if Robot.population == 0: 
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} Robots left".format(Robot.population))

    def say_hi(self):
        """Greeting by the robot"""
        print("Greetings, My master calls me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population"""
        print("We have {:d} Robots".format(cls.population))


# First Robot
droid1 = Robot("Punk-x")
droid1.say_hi()
Robot.how_many()

# Second Robot
droid2 = Robot("Mark-3")
droid2.say_hi()
Robot.how_many()

print("\nInitiating self control\n")

droid1.die()
droid2.die()

Robot.how_many()
