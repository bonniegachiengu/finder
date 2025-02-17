from setuptools import setup, find_packages

setup(
    name='finder',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'argparse'
    ],
    entry_points={
        'console_scripts': [
            'finder=finder.finder:main',
        ],
    },
)