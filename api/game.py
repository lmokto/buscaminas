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
    x = random.randrange(1, row+1)
    y = random.randrange(1, clm+1)
    return {'x': x, 'y': y}


def assigned_numbers(dimensions):
    pass


def assigned_space(dimensions):
    pass


def generate_game(**kwargs):
    level = LEVELS.get(kwargs.get('level'))
    x = level.get('dimension').get('row')
    y = level.get('dimension').get('clm')
    mines = level.get('mines')
    dimensions = generate_dimensions(x, y)
    mines_position = [random_mines(x, y) for _ in range(mines+1) if _]
    assigned_mines(dimensions, mines_position)

    return dimensions
