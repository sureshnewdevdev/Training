class Player:
    def __init__(self, pname, playerage):
        self.name = pname
        self.age = playerage
        self.speed = 0
      
    def run_registor(self, pname, page, speed):
        self.name = pname
        self.age = page
        self.speed = speed


class StatePlayer(Player):
    def __init__(self, pname, playerage, playerstate):
        super().__init__(pname, playerage)
        self.state = playerstate

    def set_state(self, pname, playerage, speed, pstate):
        super().run_registor(pname, playerage, speed)
        self.state = pstate

def display(player=None):
        print("Player Details:")
        if(type(player) is StatePlayer):
            print(f"Name: {player.name}, Age: {player.age}, Speed: {player.speed}, State: {player.state}")
        if(type(player) is Player):
            print(f"Name: {player.name}, Age: {player.age}, Speed: {player.speed}")

player = StatePlayer("Alice", 25, "Active")

display(player)


player2 = Player("Bob", 30)
display(player2)