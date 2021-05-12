"""Script to install covid_model package."""
from setuptools import setup, find_packages

with open('README.md', 'r') as rm:
    long_description = rm.read()

setup(
        name='covid_model',
        version='0.0.1',
        author='Sumukh Ghodke',
        description='Modelling COVID-19 spread',
        packages=find_packages(exclude=['tests', 'tests.*']),
        include_package_data=True,
        classifiers=['Programming Language :: Python :: 3'],
        python_requires='>=3.8',
)
