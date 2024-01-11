from setuptools import setup, find_packages

setup(
    name='MentalKita',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pandas==2.1.4',
        'matplotlib==3.8.2',
    ],
)