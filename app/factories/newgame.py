from app.factories.player import player_factory


def new_game_factory(game_name, player_count, mode, first_player):
    return {
        'gameName': game_name,
        'playerCount': player_count,
        'mode': mode,
        'characterDeck': [],
        'districtDeck': [],
        'turn': 0,
        'stage': 'character-selection',
        'players': [player_factory(first_player)]
    }
