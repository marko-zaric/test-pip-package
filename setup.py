from setuptools import setup, find_packages

setup(
    name='my_pip_package',
    version='0.0.1',

    
    author='Marko Zaric',
    author_email='m-zaric@hotmail.com',
    description='A small example package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/marko-zaric/test-pip-package',
    py_modules=find_packages(),
)