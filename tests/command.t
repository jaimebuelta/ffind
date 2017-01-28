Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $TESTDIR/../ffind/ffind.py --command "print('file:' + filename)" stest1
  file:./test_dir/second_level/stest1.py
