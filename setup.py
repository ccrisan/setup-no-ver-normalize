from setuptools import setup

setup(
    name='setupnovernormalize',
    version='1.0.1',
    py_modules=['setupnovernormalize'],
    description='Prevent version normalization when packaging Python projects with setuptools.',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ccrisan/setup-no-ver-normalize',
    author='Calin Crisan',
    author_email='ccrisan@gmail.com',
    license='UNLICENSE'
)
