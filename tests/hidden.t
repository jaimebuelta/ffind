Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $FFIND_PY --hidden config
  ./test_dir/.git/config
  ./test_dir/second_level/config
  $ $PYTHON $FFIND_PY config
  ./test_dir/second_level/config
  $ $PYTHON $FFIND_PY lib

Using environment variable

  $ FFIND_SEARCH_HIDDEN=1 $PYTHON $FFIND_PY config
  ./test_dir/.git/config
  ./test_dir/second_level/config
