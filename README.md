ffind v1.3.0 - A sane replacement for command line file search
===

[![Build Status](https://travis-ci.org/jaimebuelta/ffind.svg?branch=master)](https://travis-ci.org/jaimebuelta/ffind)
[![Coverage Status](https://coveralls.io/repos/github/jaimebuelta/ffind/badge.svg?branch=master)](https://coveralls.io/github/jaimebuelta/ffind?branch=master)
[![Requirements Status](https://requires.io/github/jaimebuelta/ffind/requirements.svg?branch=master)](https://requires.io/github/jaimebuelta/ffind/requirements/?branch=master)
[![PyPI version](https://badge.fury.io/py/ffind.svg)](https://badge.fury.io/py/ffind)
[![codecov](https://codecov.io/gh/jaimebuelta/ffind/branch/master/graph/badge.svg)](https://codecov.io/gh/jaimebuelta/ffind)

# About ffind

ffind allows quick and easy recursive search for files in the command line. Very convenient to find a file you don't know exactly where it is or how it's called in a jungle of directories. 

For example, when:

- Developing code. When it's that `.js` file? It was called my_feature_something_somethign.js, but not sure on which on of the 30 subdirectories it is. `ffind my_feature`
- Searching for a particular funny meme. It was under Images directory, but not sure if it was a .mp4 or .gif and if it was "dancing" or "DANCE"... `ffind Images/ danc`

**See it here in action!**

![Demo](https://github.com/jaimebuelta/ffind/blob/master/ffind.gif)

If you have deal with Unix `find`, it replaces the cumbersome `find . -name '*FILE_PATTERN*'` with `ffind FILE_PATTERN` (plus more niceties).

# Main features

- Search recursively on current directory by default.
- Ignores hidden and source control files and directories by default, avoiding showing files you don't care.
- If the FILE_PATTERN is all in lowercase, the search will be case insensitive, unless a flag is set.
- Will print colorized output in glamorous red (default), except on redirected output.
- Can delete matched files, making very easy to clean compiled files, like `.pyc` or `.o`. Try `ffind --delete pyc` on your Python project

Common uses:

- `ffind txt` to return all text files in current tree structure.
- `ffind ../other_dir txt` to return all text files under dir ../other_dir
- `ffind --delete pyc` to delete files that contain `pyc`. Use `ffind --delete pyc$` for only files *ending* in `pyc`

But wait, there is more!

- Input filename may be a full regex
- Regex can affect only the filename (default) or the full path.
- Follow symlinks by default, but that can be deactivated if necessary to avoid recursion problems
- Works in Python 2.7 and Python 3. **Please use Python 3.5 or later. It's much faster!**
- Can execute commands on matched files
- Experimental fuzzy search


# Install

Requires [pip](https://pip.pypa.io/en/stable/installing/), the tool for installing Python packages. You already have it installed by default on Python3!

```
pip install ffind
```

# All arguments

Call `ffind --help` to display all the available arguments.

    usage: ffind.py [-h] [-p] [--nocolor] [--nosymlinks] [--hidden] [-c]  [-i]
                [--delete | --exec "command" | --module "module_name args" | --command "program"]
                [--ignore-vcs] [-f] [--version]
                [dir] filepattern

    Search file name in directory tree

More information [here](https://github.com/jaimebuelta/ffind/blob/master/docs/ALL_ARGUMENTS.md)

# Environment variables

Environment variables in your shell can be used to set up default options and parameters. See [here](https://github.com/jaimebuelta/ffind/blob/master/docs/ENV_VARIABLES.md) for more information.


# Manual install

From the source code directory:

```
python setup.py install
```

# Test

To test ffind, you must install [cram](https://bitheap.org/cram/) (you can use `pip install cram`). To run all the tests, run `make test`. This runs the tests on both Python 2 and Python 3. Running just `make` runs the test for Python 3.

The tests are under the `tests` directory; more tests are welcome.


# License

The MIT License (MIT)

Copyright (c) 2013-2018 Jaime Buelta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
