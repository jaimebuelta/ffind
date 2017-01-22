Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $TESTDIR/../ffind/ffind.py .test..py
  ./test_dir/second_level/stest1.py
  ./test_dir/second_level/sTest2.py

Clean up
 
  $ . $TESTDIR/cleanup.sh
