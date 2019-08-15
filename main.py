from engine.engine import Engine
from engine.player import Player


if __name__ == "__main__": 
    eng = Engine()

    # Player object
    player = Player()
    eng.add_object(player)

    eng.on_execute()
