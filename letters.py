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
        'transition': 'linear'
    },
    'b': {
        'coordinates': [
            [0.0, -0.3],
            [0.0, -1.0],
        ],
        'length_override': None,
        'transition': 'linear'
    },
    'm': {
        'coordinates': [
            [0.0, 0.6, 0.1, -0.5, 0],
            [0.0, 0.2, -0.5, -1.1, -1],
        ],
        'length_override': None,
        'transition': 'linear'
    },
    'ns': {
        'coordinates': [
            [0.0, 0.5, 0, -0.2, 0.2],
            [0.0, 0.0, -0.5, 0.0, -0.05],
        ],
        'length_override': None,
        'transition': 'linear'
    },
    'dot': {
        'coordinates': [
            [0.0, 0.001],
            [0.0, 0.001],
        ],
        'length_override': 100,
        'transition': 'linear'
    },
    'skap': {
        'coordinates': [
            [0.0, 2, 0.0, 0.0, -1],
            [0.0, 0.1, 1.5, 0.0, -3],
        ],
        'length_override': 0.3,
        'transition': 'linear'
    },
}


def letter(letter):
    nodes = np.asfortranarray(conf[letter]['coordinates'])
    curve = bezier.Curve(nodes, degree=len(nodes[0]) - 1)
    if conf[letter]['length_override']:
        return curve, int(conf[letter]['length_override'] * curve.length * length_multiplier)
    else:
        return curve, int(curve.length * length_multiplier)
