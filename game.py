#python3

import numpy as np


class Map_thing:
    def __init__(self, t_char, mohs):
        self.t_char = t_char
        self.mohs = mohs

    def print_self(self):
        return self.t_char

    def get_mohs(self):
        return self.mohs

class Map:
    def __init__(self, width, height, density ):
        self.width = width
        self.height = height
        self.density = density

        self._wall = Map_thing('؅',10)
        self._space = Map_thing(' ',0)

        self._map = []

    def _init_map(self, density=None):
        den = density if density is not None else self.density
        for col in range(self.width):
            if col == 0 or col == self.width - 1:
                self._map.append([self._wall] * self.height)
            else:
                column = [self._wall]
                column.append([self._wall if np.random.randint(100) <= den else self._space for i in range(self.height - 2)])
                column.append(self._wall)
            self._map.append(column)


    def _print(self):
        map_str = ''
        for i in range(self.width):
            for j in range(self.height):
                map_str += self._map[i][j].t_char
        return map_str


if __name__ == "__main__":
    m = Map(10, 10, 50)
    print(m._print())


