Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $TESTDIR/../ffind/ffind.py --hidden lib
  ./test_dir/.git/library
  ./test_dir/.venv/library
  $ $PYTHON $TESTDIR/../ffind/ffind.py --hidden --ignore-vcs lib
  ./test_dir/.venv/library
  $ $PYTHON $TESTDIR/../ffind/ffind.py lib

  $ $PYTHON $TESTDIR/../ffind/ffind.py --hidden gitignore
  ./test_dir/.gitignore
  $ $PYTHON $TESTDIR/../ffind/ffind.py --ignore-vcs gitignore

  $ $PYTHON $TESTDIR/../ffind/ffind.py --hidden --ignore-vcs gitignore

Env variable

  $ FFIND_SEARCH_HIDDEN=1 $PYTHON $TESTDIR/../ffind/ffind.py lib
  ./test_dir/.git/library
  ./test_dir/.venv/library
  $ FFIND_SEARCH_HIDDEN=1 FFIND_IGNORE_VCS=1 $PYTHON $TESTDIR/../ffind/ffind.py lib
  ./test_dir/.venv/library
  $ FFIND_SEARCH_HIDDEN=1 $PYTHON $TESTDIR/../ffind/ffind.py gitignore
  ./test_dir/.gitignore
  $ FFIND_IGNORE_VCS=1 $PYTHON $TESTDIR/../ffind/ffind.py gitignore
