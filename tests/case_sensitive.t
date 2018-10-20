Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $FFIND_CMD test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py

  $ $FFIND_CMD -c Test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py

  $ $FFIND_CMD -c test2

  $ $FFIND_CMD -i STEST1
  ./test_dir/second_level/stest1.py

  $ $FFIND_CMD -i -c Test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py


Run the tests with environment variables

  $ $FFIND_CMD test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py

  $ FFIND_CASE_SENSITIVE=1 $FFIND_CMD Test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py

  $ FFIND_CASE_SENSITIVE=1 $FFIND_CMD test2

  $ FFIND_CASE_INSENSITIVE=1 $FFIND_CMD STEST1
  ./test_dir/second_level/stest1.py

  $ FFIND_CASE_SENSITIVE=1 FFIND_CASE_INSENSITIVE=1 $FFIND_CMD Test2
  ./test_dir/Test2.py
  ./test_dir/second_level/sTest2.py
