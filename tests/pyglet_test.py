import pyglet.lib
from pyglet.util import debug_print

_debug = debug_print('debug_media')

avutil = pyglet.lib.load_library(
    'avutil',
    win32=('avutil-57', 'avutil-56'),
    darwin=('avutil.58', 'avutil-56')
)