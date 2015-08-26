"""bayeosgatewayclient setup"""

try:
    from setuptools import setup
except ImportError as ierr:
    print 'Import error :' + str(ierr)
    from distutils.core import setup

setup(
    name='bayeosgatewayclient',
    version='0.1.9',
    packages=['bayeosgatewayclient'],
    description='A generic Python package to transfer client data to a BayEOS Gateway.',
    author='Anja Kleebaum',
    author_email='Anja.Kleebaum@stmail.uni-bayreuth.de',
    license='GPL2',
    keywords='bayeos gateway client',
    classifiers=['Programming Language :: Python'])
