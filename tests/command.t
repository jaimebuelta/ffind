Setup

  $ . $TESTDIR/setup.sh

Run test (we know the error is converting implicitly int to str, but the error is different
in different versions of python)

  $ $PYTHON $TESTDIR/../ffind/ffind.py --command "print('file:' + filename)" stest1
  file:./test_dir/second_level/stest1.py
  $ $PYTHON $TESTDIR/../ffind/ffind.py --command "print('file:' + filename + 1)" stest1
  *str* (glob)
  [1]
