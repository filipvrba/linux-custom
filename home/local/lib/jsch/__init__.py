import json

ENCODING = 'utf-8'
_data = None

def open_file( name ):
    try:
        with open(name, 'r', encoding=ENCODING) as fcc_file:
            fcc_data = json.load( fcc_file )
            set_data( fcc_data )
            return fcc_data
    except:
        set_data( { } )
        return _data


def write_file( name ):
        with open( name, 'w+', encoding=ENCODING ) as fcc_file:
            json.dump( _data, fcc_file, indent=4 )


def set_data( data ):
    global _data
    _data = data


def add_data( key, value ):
    _data[ key ] = value


def main( args ):

    if len( args ) == 3:
        file = args[0]
        key = args[1]
        value = args[2]

        open_file( file )
        add_data( key, value )
        write_file( file )
    else:
        print( "Add an 3 arguments (file, key, value)!" )
