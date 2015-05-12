''' Setup / installation script '''
from distutils.core import setup
from distutils.command.install import install
import os
import subprocess

from future import print_function


def abspath(path):
    """A method to determine absolute path
    for a relative path inside project's directory."""

    return os.path.abspath(os.path.join(os.path.dirname(__file__), path))


class ff_install(install):

    def run(self):

        install.run(self)

        man_dir = abspath("./man_pages/")

        output = subprocess.Popen([os.path.join(man_dir, "install.sh")],
                stdout=subprocess.PIPE,
                cwd=man_dir,
                universal_newlines=True,
                env=dict({"PREFIX": self.prefix},
                         **dict(os.environ))).communicate()[0]
        print(output)


setup(
    # metadata
    name='ffind',
    description='Sane replacement for command line file search',
    license='MIT',
    version='0.8',
    author='Jaime Buelta',
    author_email='jaime.buelta@gmail.com',
    url='https://github.com/jaimebuelta/ffind',
    download_url='https://github.com/jaimebuelta/ffind/tarball/0.8',
    platforms='Cross Platform',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'setuptools',
    ],
    keywords=['searching', 'file system'],
    packages=['ffind', 'ffind.backports'],
    scripts=['scripts/ffind'],
    cmdclass={"install": ff_install},
)
