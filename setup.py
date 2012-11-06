''' Setup / installation script '''
from distutils.core import setup

setup(
    # metadata
    name='ffind',
    description='Sane replacement for find',
    license='Public domain',
    version='0.1',
    author='Jaime Buelta',
    platforms='Cross Platform',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    packages=['ffind'],
    scripts=['scripts/ffind'],
)
