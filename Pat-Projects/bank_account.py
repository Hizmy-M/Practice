class Games:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"{self.name} and {self.age}") 
    
# comments added
class Store:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)
        print(f'Game added {game.name}')
        game.display_info()



game_one = Games('GTA', 12)

game_store = Store()
game_store.add_game(game_one)
