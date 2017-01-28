Setup

  $ . $TESTDIR/setup.sh

Run test

Ensure consistent sorting, as this depends on the filesystem

  $ $PYTHON $TESTDIR/../ffind/ffind.py --hidden config | sort
  ./test_dir/.git/config
  ./test_dir/second_level/config
  $ $PYTHON $TESTDIR/../ffind/ffind.py config
  ./test_dir/second_level/config
  $ $PYTHON $TESTDIR/../ffind/ffind.py lib
