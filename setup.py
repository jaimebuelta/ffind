from __future__ import print_function
''' Setup / installation script '''

from setuptools import setup
from setuptools.command.install import install
from setuptools import find_packages

import os
import subprocess


def abspath(path):
    """A method to determine absolute path
    for a relative path inside project's directory."""

    return os.path.abspath(os.path.join(os.path.dirname(__file__), path))


class ff_install(install):

    def run(self):

        install.run(self)

        man_dir = abspath("./man_pages/")

        cmd = subprocess.Popen([os.path.join(man_dir, "install.sh")],
                               stdout=subprocess.PIPE,
                               cwd=man_dir,
                               universal_newlines=True,
                               env=dict({"PREFIX": self.prefix},
                                        **dict(os.environ)))
        output = cmd.communicate()[0]
        print(output)


setup(
    # metadata
    name='ffind',
    description='Sane replacement for command line file search',
    license='MIT',
    version='1.5.0',
    author='Jaime Buelta',
    author_email='jaime.buelta@gmail.com',
    url='https://github.com/jaimebuelta/ffind',
    download_url='https://github.com/jaimebuelta/ffind/tarball/v1.5.0',
    platforms='Cross Platform',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    install_requires=['setuptools'],
    python_requires='>=3.7, <4',
    keywords=['searching', 'file system'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': ['ffind = ffind.ffind:run'],
    },
    cmdclass={"install": ff_install},
)
