Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $FFIND_CMD --hidden config
  ./test_dir/.git/config
  ./test_dir/second_level/config
  $ $FFIND_CMD config
  ./test_dir/second_level/config
  $ $FFIND_CMD lib

Using environment variable

  $ FFIND_SEARCH_HIDDEN=1 $FFIND_CMD config
  ./test_dir/.git/config
  ./test_dir/second_level/config
