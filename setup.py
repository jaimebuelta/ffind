''' Setup / installation script '''
from distutils.core import setup

setup(
    # metadata
    name='ffind',
    description='Sane replacement for find',
    license='MIT',
    version='0.2',
    author='Jaime Buelta',
    author_email='jaime.buelta@gmail.com',
    url='https://github.com/jaimebuelta/ffind',
    download_url='https://github.com/jaimebuelta/ffind/tarball/0.2',
    platforms='Cross Platform',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords=['searching', 'file system'],
    packages=['ffind'],
    scripts=['scripts/ffind'],
)
