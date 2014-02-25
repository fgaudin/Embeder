from distutils.core import setup
from setuptools import find_packages

setup(
    name='Embeder',
    version='0.1.0',
    author='Francois Gaudin',
    author_email='contact@francoisgaudin.com',
    packages=find_packages(),
    url='http://pypi.python.org/pypi/Embeder/',
    license='LICENSE.txt',
    description='Retrieves useful information about a link.',
    long_description=open('README.rst').read(),
    install_requires=[
        "beautifulsoup4 == 4.3.2",
        "requests == 1.1.0"
    ],
)
