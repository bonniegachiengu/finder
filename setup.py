from setuptools import setup, find_packages

setup(
    name='Finder',
    version='0.1.0',
    author='Bonnie Gachiengu',
    author_email='bonniegachiengu@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'argparse'
    ],
)