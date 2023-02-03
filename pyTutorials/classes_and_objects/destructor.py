#!/usr/bin/python3
class Robot:
    def __inti__(self, name, build_year):
        """Initialized a robot"""
        self.name = name
        self.build_year = build_year
        print("Initialized Robot: {}".format(self.name))

    def __del__(self):
        """Destroys a robot"""
        print("Destroying Robot: {}".format(self.name))

    #Setter Methods
    def set_name(self, name):
        """Sets the name"""
        self.name = name
        print("Name of this robot has been set to {}".format(self.name))

    def set_buildYear(self, build_year):
        """Sets the build year"""
        self.build_year = build_year
        print("Build Year of this robot has been set to {}".format(self.build_year))
    # Getter Methods
    def get_name(self):
        """Gets the name"""
        return self.name

    def get_buildYear(self):
        """Gets the build year"""
        return self.build_year

x = Robot()
x.set_name("Mark-233")
x.set_buildYear(1999)
y = Robot()
y.set_name("Cali-43")
y.set_buildYear(1843)

# Destroying the robots
for rob in [x,y]:
    del rob

