Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $FFIND_PY test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py

  $ $PYTHON $FFIND_PY -c Test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py

  $ $PYTHON $FFIND_PY -c test2

  $ $PYTHON $FFIND_PY -i STEST1
  ./test_dir/second_level/stest1.py

  $ $PYTHON $FFIND_PY -i -c Test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py


Run the tests with environment variables

  $ $PYTHON $FFIND_PY test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py

  $ FFIND_CASE_SENSITIVE=1 $PYTHON $FFIND_PY Test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py

  $ FFIND_CASE_SENSITIVE=1 $PYTHON $FFIND_PY test2

  $ FFIND_CASE_INSENSITIVE=1 $PYTHON $FFIND_PY STEST1
  ./test_dir/second_level/stest1.py

  $ FFIND_CASE_SENSITIVE=1 FFIND_CASE_INSENSITIVE=1 $PYTHON $FFIND_PY Test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py
