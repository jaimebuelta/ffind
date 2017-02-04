ffind v1.0.4 - A sane replacement for command line file search
===

*Info:* An utility to search files recursively on a dir.

*Author:* Jaime Buelta

[![Build Status](https://travis-ci.org/jaimebuelta/ffind.svg?branch=master)](https://travis-ci.org/jaimebuelta/ffind)
[![Coverage Status](https://coveralls.io/repos/github/jaimebuelta/ffind/badge.svg?branch=master)](https://coveralls.io/github/jaimebuelta/ffind?branch=master)
[![Requirements Status](https://requires.io/github/jaimebuelta/ffind/requirements.svg?branch=master)](https://requires.io/github/jaimebuelta/ffind/requirements/?branch=master)
[![PyPI version](https://badge.fury.io/py/ffind.svg)](https://badge.fury.io/py/ffind)

About
---

Basically, replaces `find . -name '*FILE_PATTERN*'` with `ffind.py FILE_PATTERN`

- Input filename maybe a regex
- Search recursively on current directory by default.
- If the FILE_PATTERN is all in lowercase, the search will be case insensitive, unless a flag is set.
- Regex can affect only the filename (default) or the full path.
- Will print colorized output in glamorous red (default), except on redirected output.
- Ignores hidden directories (directories starting with .) by default, but this can be disabled
- Can ignore source control common directories
- Follow symlinks by default, but that can be deactivated if necessary to avoid recursion problems
- Works in python2.7 and python3. **It is recommended in Python 3.5 or later due performance improvements. It's much faster!**
- Can delete matched files
- Can execute a command on matched files
- Experimental fuzzy search

Common uses:

- `ffind txt` to return all text files in current dir
- `ffind ../other_dir txt` to return all text files under dir ../other_dir (or `ffind.py txt -d ../other_dir`)


All options
---

    usage: ffind.py [-h] [-p] [--nocolor] [--nosymlinks] [--hidden] [-c]
                [--delete | --exec "command" | --module "module_name args" | --command "program"]
                [--ignore-vcs] [-f] [--version]
                [dir] filepattern

    Search file name in directory tree

    positional arguments:
      dir                   Directory to search
      filepattern

    optional arguments:
      -h, --help            show this help message and exit
      -p                    Match whole path, not only name of files
      --nocolor             Do not display color
      --nosymlinks          Do not follow symlinks (following symlinks can lead to
                            infinite recursion)
      --hidden              Do not ignore hidden directories
      -c                    Force case sensitive. By default, all lowercase
                            patterns are case insensitive
      --delete              Delete files found
      --exec "command"      Execute the given command with the file found as
                            argument. The string '{}' will be replaced with the
                            current file name being processed. If this option is
                            used, ffind will return a status code of 0 if all the
                            executions return 0, and 1 otherwise
      --module "module_name args"
                            Execute the given module with the file found as
                            argument. The string '{}' will be replaced with the
                            current file name being processed. If this option is
                            used, ffind will return a status code of 0 if all the
                            executions return 0, and 1 otherwise. Only SystemExit
                            is caught
      --command "program"   Execute the given python program with the file found
                            placed in local variable 'filename'. If this option is
                            used, ffind will return a status code of 1 if any
                            exceptions occur, and 0 otherwise. SystemExit is not
                            caught
      --ignore-vcs          Ignore version control system files and directories
      -f                    Experimental fuzzy search. Increases the matches, use
                            with care. Combining it with regex may give crazy
                            results
      --version             show program's version number and exit


Install
---
pip install ffind

Manual Install
---

python setup.py install

Test
---
It requires to install [cram](https://bitheap.org/cram/) (it can be installed with `pip install cram`)

To run all the tests, run `make test`. This runs the tests on both Python 2 and Python 3. Running just
`make` runs the test for Python 3.

The tests are under the `tests` directory, more tests are welcome.
