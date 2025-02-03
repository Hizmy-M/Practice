class Game:
    def __init__(self, game_id, game_name, game_type):
        self.game_id = game_id
        self.game_name = game_name
        self.game_type = game_type

    def display_info(self):
        return f'{self.game_name} is a {self.game_type}'


class Store:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)
        print(f'{game.game_name} added successfully')

    def remove_game(self, id):
        for game in self.games:
            if id == game.game_id:
                print('Game available removed')
                return

        print('No games')


one_game = Game(44, 'GTA', 'Open')
one_store = Store()

one_store.add_game(one_game)
one_store.remove_game(44)
one_store.remove_game(7)

