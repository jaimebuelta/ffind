ffind v1.2.0 - A sane replacement for command line file search
===

*Info:* An utility to search files recursively on a dir.

*Author:* Jaime Buelta

[![Build Status](https://travis-ci.org/jaimebuelta/ffind.svg?branch=master)](https://travis-ci.org/jaimebuelta/ffind)
[![Coverage Status](https://coveralls.io/repos/github/jaimebuelta/ffind/badge.svg?branch=master)](https://coveralls.io/github/jaimebuelta/ffind?branch=master)
[![Requirements Status](https://requires.io/github/jaimebuelta/ffind/requirements.svg?branch=master)](https://requires.io/github/jaimebuelta/ffind/requirements/?branch=master)
[![PyPI version](https://badge.fury.io/py/ffind.svg)](https://badge.fury.io/py/ffind)
[![codecov](https://codecov.io/gh/jaimebuelta/ffind/branch/master/graph/badge.svg)](https://codecov.io/gh/jaimebuelta/ffind)

About
---

It allows quick and easy recursive search for files in the Unix command line. 
Basically, replaces `find . -name '*FILE_PATTERN*'` with `ffind.py FILE_PATTERN` (and a few more niceties)

![Demo](https://github.com/jaimebuelta/ffind/blob/master/ffind.gif)

- Input filename may be a regex
- Search recursively on current directory by default.
- If the FILE_PATTERN is all in lowercase, the search will be case insensitive, unless a flag is set.
- Regex can affect only the filename (default) or the full path.
- Will print colorized output in glamorous red (default), except on redirected output.
- Ignores hidden directories (directories starting with `.`) by default, but this can be disabled
- Can ignore source control common directories, like `.git` or `.svn`
- Follow symlinks by default, but that can be deactivated if necessary to avoid recursion problems
- Works in python2.7 and python3. **It is recommended in Python 3.5 or later due performance improvements. It's much faster!**
- Can delete matched files
- Can execute a command on matched files
- Experimental fuzzy search

Common uses:

- `ffind txt` to return all text files in current dir
- `ffind ../other_dir txt` to return all text files under dir ../other_dir (or `ffind.py txt -d ../other_dir`)

Install
---
Requires [pip](https://pip.pypa.io/en/stable/installing/), the tool for installing Python packages.

```
pip install ffind
```

All options
---

    usage: ffind.py [-h] [-p] [--nocolor] [--nosymlinks] [--hidden] [-c]  [-i]
                [--delete | --exec "command" | --module "module_name args" | --command "program"]
                [--ignore-vcs] [-f] [--version]
                [dir] filepattern

    Search file name in directory tree

    positional arguments:
      dir                   Directory to search
      filepattern

    optional arguments:
      -h, --help            show this help message and exit
      -p                    Match whole path, not only name of files. Set env
                            variable FFIND_SEARCH_PATH to set this automatically
      --nocolor             Do not display color. Set env variable FFIND_NO_COLOR
                            to set this automatically
      --nosymlinks          Do not follow symlinks (following symlinks can lead to
                            infinite recursion) Set env variable FFIND_NO_SYMLINK
                            to set this automatically
      --hidden              Do not ignore hidden directories. Set env variable
                            FFIND_SEARCH_HIDDEN to set this automatically
      -c                    Force case sensitive. By default, all lowercase
                            patterns are case insensitive. Set env variable
                            FFIND_CASE_SENSITIVE to set this automatically
      -i                    Force case insensitive. This allows case insensitive
                            for patterns with uppercase. If both -i and -c are
                            set, the search will be case sensitive.Set env
                            variable FFIND_CASE_INSENSITIVE to set this
                            automatically
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
      --ignore-vcs          Ignore version control system files and directories.
                            Set env variable FFIND_IGNORE_VCS to set this
                            automatically
      -f                    Experimental fuzzy search. Increases the matches, use
                            with care. Combining it with regex may give crazy
                            results
      --return-results      For testing purposes only. Please ignore
      --version             show program's version number and exit

Environment variables
---

Setting these environment variables, you'll set options by default. For example:

    export FFIND_CASE_SENSITIVE=1
    # equivalent to ffind -c something
    ffind something 
    FFIND_CASE_SENSITIVE=1 ffind something

- FFIND_SORT: Return the results sorted. This is slower, and is mainly thought to ensure
              consistency on the tests, as some filesystems may order files differently
- FFIND_CASE_SENSITIVE: Search is case sensitive. Equivalent to `-c` flag
- FFIND_CASE_INSENSITIVE: Search is case insensitive. Equivalent to `-i` flag.
- FFIND_SEARCH_HIDDEN: Search in hidden directories. Equivalent to `--hidden` flag.
- FFIND_SEARCH_PATH: Search in the whole path. Equivalent to `-p` flag.
- FFIND_IGNORE_VCS: Ignore paths in version control. Equivalent to `--ignore-vcs`
- FFIND_NO_SYMLINK: Do not follow symlinks. Equivalent to `--nosymlinks` flag.
- FFIND_NO_COLOR: Do not show colors. Equivalent to `--nocolor` flag.
- FFIND_FUZZY_SEARCH: Enable fuzzy search. Equivalent to `-f` flag.

If an environment variable is present, when calling `ffind -h`, the option will display [SET] at the end.

Manual Install
---

From the source code directory
```
python setup.py install
```

Test
---
It requires to install [cram](https://bitheap.org/cram/) (it can be installed with `pip install cram`)

To run all the tests, run `make test`. This runs the tests on both Python 2 and Python 3. Running just
`make` runs the test for Python 3.

The tests are under the `tests` directory, more tests are welcome.
