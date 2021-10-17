import numpy as np
import bezier

length_multiplier = 20

conf = {
    'a': {
        'coordinates': [
            [0.0, 0.5],
            [0.0, 0.2],
        ],
        'length_override': None,
        'terminate': None,
        'transition': 'linear'
    },
    'b': {
        'coordinates': [
            [0.0, -0.3],
            [0.0, -1.0],
        ],
        'length_override': None,
        'terminate': None,
        'transition': 'linear'
    },
    'm': {
        'coordinates': [
            [0.0, 0.6, 0.1, -0.5, 0],
            [0.0, 0.2, -0.5, -1.1, -1],
        ],
        'length_override': None,
        'terminate': None,
        'transition': 'linear'
    },
    'ns': {
        'coordinates': [
            [0.0, 0.5, 0, -0.2, 0.2],
            [0.0, 0.0, -0.5, 0.0, -0.05],
        ],
        'length_override': None,
        'terminate': None,
        'transition': 'linear'
    },
    'dot': {
        'coordinates': [
            [0.0, 0.001],
            [0.0, 0.001],
        ],
        'length_override': 100,
        'terminate': 1,
        'transition': 'linear'
    },
    'skap': {
        'coordinates': [
            [0.0, 2, 0.0, 0.0, -1],
            [0.0, 0.1, 1.5, 0.0, -3],
        ],
        'length_override': 0.3,
        'terminate': None,
        'transition': 'linear'
    },
}


def letter(letter):
    nodes = np.asfortranarray(conf[letter]['coordinates'])
    curve = bezier.Curve(nodes, degree=len(nodes[0]) - 1)

    if conf[letter]['length_override']:
        length = int(conf[letter]['length_override'] * curve.length * length_multiplier)
    else:
        length = int(curve.length * length_multiplier)

    return curve, length, conf[letter]['terminate']