class Game:
    def __init__(self, game_name, game_id, game_type):
        self.game_name = game_name
        self.game_id = game_id
        self.game_type = game_type

    def game_details(self):
        print(f'ID: {self.game_id}')
        print(f'Name: {self.game_name}')
        print(f'Game Type {self.game_type}')

class Store:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)
        print(f'{game.game_name} Added....')

    def remove_game(self, id):
        for game in self.games:
            if id == game.game_id:
                self.games.remove(game)
                print('Removed')
                return

        print('No Game')




