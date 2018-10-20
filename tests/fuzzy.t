Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $FFIND_CMD e1
  $ $FFIND_CMD -f e1
  ./test_dir/test1.py
  ./test_dir/second_level/stest1.py

Using environment variable

  $ FFIND_FUZZY_SEARCH=1 $FFIND_CMD -f e1
  ./test_dir/test1.py
  ./test_dir/second_level/stest1.py
