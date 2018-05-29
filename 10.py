class Gym:
    totalMembers = 0

    def __init__(self, name="Aquapark", price=1000, members=10, location="Kn Olhy", working_hours="from 6 to 22"):
        self.__name = name
        self.price = price
        self.members = members
        self.location = location
        self.working_hours = working_hours
        Gym.totalMembers += members

    def to_string(self):
        print("Name: " + self.name + "; Price:", self.price,
              "; Members:", self.members, "; Location:", self.location, "; Working hours:", self.working_hours, ";")

    def print_sum(self):
        print("Members: " + self.name + ": ", self.members, ";")

    @staticmethod
    def print_static_sum():
        print("Total members: ", Gym.totalMembers, ";")



aquapark = Gym()
sport_life = Gym("Sport Life ", 4500, 160, "Heroiv UPA", "from 8 to 23")
king_hall = Gym("Aquapark ", 3000, 210, "Naukova")

print("\n")
sport_life.to_string()
aquapark.to_string()
king_hall.to_string()

print("\n")
sport_life.print_sum()
aquapark.print_sum()
king_hall.print_sum()

print("\n")
Gym.print_static_sum()