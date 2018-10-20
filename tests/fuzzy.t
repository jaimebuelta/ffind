Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $FFIND_PY e1
  $ $PYTHON $FFIND_PY -f e1
  ./test_dir/test1.py
  ./test_dir/second_level/stest1.py

Using environment variable

  $ FFIND_FUZZY_SEARCH=1 $PYTHON $FFIND_PY -f e1
  ./test_dir/test1.py
  ./test_dir/second_level/stest1.py
