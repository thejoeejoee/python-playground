from collections import defaultdict
import re
from sys import stdin


def sum_total_lit_lights(commands):
    plan = defaultdict(default_factory=lambda: False)

    def _apply_on_rectangle(x0, y0, x1, y1, f):
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                plan.update({(x, y): f(plan.get((x, y)))})

    functions = {
        'turn on': lambda v: True,
        'turn off': lambda v: False,
        'toggle': lambda v: not v
    }
    regex = re.compile(r'([\w\s]+) (\d+),(\d+) through (\d+),(\d+)', re.IGNORECASE)
    for command in commands:
        """
        toggle 857,493 through 989,970
        turn on 631,950 through 894,975
        turn off 341,716 through 462,994
        """
        match = regex.match(command)
        if match:
            fce, x0, y0, x1, y1 = match.groups()
            print('Applying {} on {},{} -> {},{}'.format(fce, x0, y0, x1, y1))
            _apply_on_rectangle(int(x0), int(y0), int(x1), int(y1), f=functions.get(fce))

    return sum(int(plan.get((x, y), 0)) for x in range(1000) for y in range(1000))


if __name__ == '__main__':
    print(sum_total_lit_lights(stdin.readlines()))