Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $TESTDIR/../ffind/ffind.py --hidden lib
  ./test_dir/.git/library
  ./test_dir/.venv/library
  $ $PYTHON $TESTDIR/../ffind/ffind.py --hidden --ignore-vcs lib
  ./test_dir/.venv/library
  $ $PYTHON $TESTDIR/../ffind/ffind.py lib
