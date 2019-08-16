from engine.engine import Engine
from engine.player import Player
from engine.level import Level

if __name__ == "__main__":
    eng = Engine()

    # Player object
    player = Player()
    eng.add_player(player)

    # Generate level
    level = Level(eng)
    level.load_level(1)

    eng.on_execute()
