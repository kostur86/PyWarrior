import os.path

from engine.object import Tree

class LevelError(Exception):
    """
    """


class Level(object):
    levels_path = "levels"
    levels_ext = "txt"

    def __init__(self, engine):
        """
        """
        self._engine = engine

    def load_level(self, level_num):
        """
        """
        level_path = os.path.join(
            Level.levels_path,
            "level_{:02d}.{}".format(level_num, Level.levels_ext)
        )

        if not os.path.exists(level_path):
            raise LevelError(
                "Eror when loading level: "
                "level {} does not exists".format(level_num)
            )

        row = 0

        with open(level_path, 'r') as level:
            for line in level.readlines():
                column = 0

                for obj in line.split():

                    if obj == "P":
                        self._engine.get_player().set_position(column, row)
                    elif obj == "T":
                        tree = Tree("green_ball_sprite.png")
                        tree.set_position(column, row)
                        self._engine.add_object(tree)

                    column += 1
                row += 1
