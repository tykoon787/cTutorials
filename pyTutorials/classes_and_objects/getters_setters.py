class Robot:
    def __init__(self, name, build_year: int): 
        self.name = name
        self.build_year = build_year
        print("Initialized Robot {}".format(self.name))

    def say_hi(self):
        if (self.name and self.build_year):
            print("Hi, My name is {}. I was built in the year {}".format(self.name, self.build_year))
        else:
            print("Hi, I am a robot without a name and build year")

    # Setter Methods
    def set_name(self, name):
       self.name = name 

    def set_buildYear(self, build_year: int):
        self.build_year = build_year

    # Getter Methods
    def get_name(self):
        return self.name

    def get_buildYear(self):
        return self.build_year

x = Robot("Mark-33", 1544)
x.say_hi()

y = Robot("", 0)
y.say_hi()
y.set_name("Droid-AA")
y.say_hi()

z = Robot("", 0)
z.set_buildYear(1993)
z.set_name("Mx-13")
z.say_hi()
