Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $TESTDIR/../ffind/ffind.py test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py

  $ $PYTHON $TESTDIR/../ffind/ffind.py -c Test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py

  $ $PYTHON $TESTDIR/../ffind/ffind.py -c test2

  $ $PYTHON $TESTDIR/../ffind/ffind.py -i STEST1
  ./test_dir/second_level/stest1.py

  $ $PYTHON $TESTDIR/../ffind/ffind.py -i -c Test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py
