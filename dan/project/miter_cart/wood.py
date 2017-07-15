from solid import *
from solid.utils import *

import prettytable

wood_bom_columns = [
    'name',
    'count',
    'type',
    'width',
    'length',
    'thickness'
]

wood_bom_table = {}

def wood_bom_update( name, *args, **kwargs ):
    if name not in wood_bom_table:
        row = {
            'name': name,
            'count': 0,
            'type': kwargs.get( 'type', "" ),
            'width': kwargs.get( 'width', "" ),
            'length': kwargs.get( 'length', "" ),
            'thickness': kwargs.get( 'thickness', "" ),
        }

        wood_bom_table[name] = row

    wood_bom_table[name]['count'] += 1

def wood( size ):
    wood_bom_update( 'x'.join(str(x) for x in size) )
    return cube( size )

def wood_2x6( length ):
    wood_bom_update( '2x6x' + str(length), type="2x6", length=length )
    return cube( [length, 1.5, 5.5] )

def wood_2x4( length ):
    wood_bom_update( '2x4x' + str(length), type="2x4", length=length )
    return cube( [length, 1.5, 3.5] )

def plywood( width, length, thickness=.5 ):
    wood_bom_update( 'plywood ' + str(width) + 'x' + str(length), type="plywood", width=width, length=length, thickness=thickness )
    return cube( [width, length, thickness] )

def cube_rot( order ):
    def call_fn( c ):
        l = c.params['size']
        l.sort()
        l = [l[order[0]], l[order[1]], l[order[2]]]
        c.params['size'] = l
        return c

    return call_fn

def wood_bom():
    table = prettytable.PrettyTable( field_names=wood_bom_columns )

    for k, v in wood_bom_table.items():
        table.add_row( [v[n] for n in wood_bom_columns] )

    return table.get_string()
