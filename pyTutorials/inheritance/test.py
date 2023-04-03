class Base():
    """My Base Class"""
    __nb_instances = 0
    def __init__ (self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances
        print("Initalized one base class\n")

class User(Base):
    """My User Class"""
    pass
    # def __init__(self):
    #     super().__init__()
    #     self.id += 99

if __name__ == '__main__':
    for i in range(4):
        print(User().id)