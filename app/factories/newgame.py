from app.factories.player import player_factory

def new_game_factory(name, players, mode, first_player):
    # print(player_factory(first_player))
    return {
        'name': name,
        'playerCount': players,
        'mode': mode,
        'characterDeck': [],
        'districtDeck': [],
        'turn': 0,
        'stage': 'character-selection',
        'players': [player_factory(first_player)]
    }