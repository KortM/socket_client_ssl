from distutils.core import setup
import py2exe

setup(
    console = ['socket_client.py'],
    options={'py2exe': {'includes': ['schedule', 'win10toast']}}
)