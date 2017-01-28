Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $TESTDIR/../ffind/ffind.py test1
  ./test_dir/test1.py
  ./test_dir/second_level/stest1.py
  $ $PYTHON $TESTDIR/../ffind/ffind.py --delete stest1
  $ $PYTHON $TESTDIR/../ffind/ffind.py test1
  ./test_dir/test1.py
