import random

LEVELS = {
    'beginner': {
        'dimension': {'row': 8, 'clm': 8},
        'mines': 10
    },
    'intermediate': {
        'dimension': {'row': 16, 'clm': 16},
        'mines': 40
    },
    'expert': {
        'dimension': {'row': 16, 'clm': 30},
        'mines': 99
    }
}


def generate_dimensions(row, clm, custom=False):
    """
    :param row: int(8)
    :param clm: int(8)
    :return: dict({
        1: {1: {'mine':False, number:0}, 2: {'mine':False,number:1}, 3: {'mine':False,number:0}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}},
        2: {1: {'mine':True, number:None}, 2: {'mine'False, number:1}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}},
        3: {1: {'mine'False,number1}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}},
        4: {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}},
        5: {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}},
        6: {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}},
        7: {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}},
        8: {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}},
        9: {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}},
        level : 'beginner': {
            'dimension': {'row': 16, 'clm': 30},
            'mines': 99
        }
    })

    no existe mina alrededor y la celda esta vacia (number=0) {'mine':False, number:0}
    celda con mina (number=None) {'mine':True, number:None}
    existe una mina a su alrededor (number=1) {'mine':False, number:1}
    """
    level = validate_level(row, clm)
    if level or custom:
        obj = {}
        for i in range(1, row + 1):
            obj.update({i: {x: {'mine': False, 'number': 0} for x in range(1, clm + 1) if x}})
        obj.update({'level': level})
        return obj
    return False


def validate_level(row, clm):
    """
    :param row: int(8)
    :param clm: int(8)
    :return: str(beginner)
    """
    if row == 8 and clm == 8:
        return 'beginner'
    elif row == 16 and clm == 16:
        return 'intermediate'
    elif row == 16 and clm == 32:
        return 'expert'
    return False


def assigned_mines(dimensions, mines_position):
    for m in mines_position:
        x = m.get('x')
        y = m.get('y')
        dimensions.get(x).get(y).update({'mine': True, 'number': None})


def random_mines(row, clm):
    x = random.randrange(1, row + 1)
    y = random.randrange(1, clm + 1)
    return {'x': x, 'y': y}


def check_min_max(v, min=1, max=9):
    x, y = v[0], v[1]
    min_max = list(range(min, max))
    if x in min_max and y in min_max:
        return x, y
    return 0, 0


def get_positions(dimensions, x, y, exclude=[]):
    positions = {}
    map_pos = {
        'c': check_min_max([x, y]),  # center
        'cr': check_min_max([x, y + 1]),  # center right dimensions.get(x).get(y + 1)
        'cl': check_min_max([x, y - 1]),  # center left dimensions.get(x).get(y - 1)
        'cu': check_min_max([x - 1, y]),  # center up dimensions.get(x - 1).get(y)
        'cul': check_min_max([x - 1, y - 1]),  # center up left dimensions.get(x - 1).get(y - 1)
        'cur': check_min_max([x - 1, y + 1]),  # center up right dimensions.get(x - 1).get(y + 1)
        'cd': check_min_max([x + 1, y]),  # center down dimensions.get(x + 1).get(y)
        'cdl': check_min_max([x + 1, y - 1]),  # center down left dimensions.get(x + 1).get(y - 1)
        'cdr': check_min_max([x + 1, y + 1])  # center down right dimensions.get(x + 1).get(y + 1)
    }
    for k, v in map_pos.items():
        if k not in exclude:
            if v[0] != 0 and v[1] != 0:
                positions.update({k: dimensions.get(v[0]).get(v[1])})
            else:
                positions.update({k: None})
    return positions


def mines_adjacent(dimensions, x, y):
    sides = ['cdl', 'cul', 'cr', 'cl', 'cu', 'cur', 'cd', 'c', 'cdr']
    center = dimensions.get(x).get(y)
    mc = 0
    if not center.get('mine') and center.get('number') == 0:
        search_mines = get_positions(dimensions, x, y)
        for k in sides:
            if search_mines.get(k):
                mc += 1 if search_mines.get(k).get('mine') else 0
        center.update({'number': mc if mc >= 1 else 'space'})


def assigned_numbers(dimensions):
    for x, v in dimensions.items():
        if type(v) == dict:
            for y, c in v.items():
                mines_adjacent(dimensions, x, y)


def filter_by_key(buscaminas, **kwargs):
    """
    :param buscaminas:
    :param kwargs: key="mines", equal=[True], dict=True
    :return:
    """
    key = kwargs.get('key')
    equal = kwargs.get('equal')
    dict = kwargs.get('dict', None)
    l = {}
    for k, v in buscaminas.items():
        l_clm = []
        if type(k) == int:
            for b in buscaminas.get(k):
                if buscaminas.get(k).get(b).get(key) in equal:
                    if dict:
                        l_clm.append({b: buscaminas.get(k).get(b).get(key)})
                    else:
                        l_clm.append(b)
            l.update({str(k): l_clm})
    return l


def generate_buscaminas(**kwargs):
    level = LEVELS.get(kwargs.get('level'))
    x = level.get('dimension').get('row')
    y = level.get('dimension').get('clm')
    mines = level.get('mines')
    dimensions = generate_dimensions(x, y)
    mines_position = [random_mines(x, y) for _ in range(mines + 1) if _]
    assigned_mines(dimensions, mines_position)
    assigned_numbers(dimensions)
    return dimensions
