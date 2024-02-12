from setuptools import setup

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/marko-zaric/test-pip-package',
    author='Marko Zaric',
    author_email='m-zaric@hotmail.com',

    py_modules=['my_pip_package'],
)