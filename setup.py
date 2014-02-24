from distutils.core import setup

setup(
    name='Embeder',
    version='0.1.0',
    author='Francois Gaudin',
    author_email='contact@francoisgaudin.com',
    packages=['embeder', 'embeder.test'],
    url='http://pypi.python.org/pypi/Embeder/',
    license='LICENSE.txt',
    description='Retrieves useful information about a link.',
    long_description=open('README.txt').read(),
    install_requires=[
        "beautifulsoup4 == 4.3.2",
        "requests == 1.1.0"
    ],
)
