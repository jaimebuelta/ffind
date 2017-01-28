Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $TESTDIR/../ffind/ffind.py --command "print('file:' + filename)" stest1
  file:./test_dir/second_level/stest1.py
  $ $PYTHON $TESTDIR/../ffind/ffind.py --command "print('file:' + filename + 1)" stest1
  *str*int* (glob)
  [1]
