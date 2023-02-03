#!/usr/bin/python3
class Robot:
    def __inti__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year
        print("Initialized {}".format(self.__name))

    def say_hi(self):
        if self.__name:
            print("Hi, My name is {}".format(self.__name))
        else:
            print("Hi. I am a robot without a name")

    # Setter Methods
    def set_name(self, name):
        """Sets the name"""
        self.__name = name

    def set_buildYear(self, build_year):
        """Sets the build year"""
        self.__build_year = build_year
        
    # Getter Methods
    def get_name(self):
        """Gets the name"""
        return self.__name

    def get_buildYear(self):
        """Gets the build year"""
        return self.__build_year

    # str() and repr()
    def __repr__(self):
        return "Robot {:s} build year {}".format(self.__name, str(self.__build_year))

    def __str__(self):
        return "Name: {}, Build Year: {}".format(self.__name, str(self.__build_year))

if __name__ == "__main__":
    x = Robot()
    x.set_name("Mark-x23")
    x.set_buildYear(1844)
    y = Robot()
    y.set_name("Cali-99")
    y.set_buildYear(2004)
    for rob in [x,y]:
        if rob.get_name() == "Cali-99":
            rob.set_buildYear(1993)
        print("Robot: {} I was built in the year {}".format(rob.get_name(), str(rob.get_buildYear())))
