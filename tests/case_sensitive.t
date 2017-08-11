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


Run the tests with environment variables

  $ $PYTHON $TESTDIR/../ffind/ffind.py test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py

  $ FFIND_CASE_SENSITIVE=1 $PYTHON $TESTDIR/../ffind/ffind.py Test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py

  $ FFIND_CASE_SENSITIVE=1 $PYTHON $TESTDIR/../ffind/ffind.py test2

  $ FFIND_CASE_INSENSITIVE=1 $PYTHON $TESTDIR/../ffind/ffind.py STEST1
  ./test_dir/second_level/stest1.py

  $ FFIND_CASE_SENSITIVE=1 FFIND_CASE_INSENSITIVE=1 $PYTHON $TESTDIR/../ffind/ffind.py Test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py
