Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $TESTDIR/../ffind/ffind.py second
  ./test_dir/second_level

  $ $PYTHON $TESTDIR/../ffind/ffind.py -p second
  ./test_dir/second_level
  ./test_dir/second_level/CVS
  ./test_dir/second_level/config
  ./test_dir/second_level/sTest2.py
  ./test_dir/second_level/stest1.py
  ./test_dir/second_level/stest3.sh
  ./test_dir/second_level/third_level

Using env variable

  $ FFIND_SEARCH_PATH=1 $PYTHON $TESTDIR/../ffind/ffind.py second
  ./test_dir/second_level
  ./test_dir/second_level/CVS
  ./test_dir/second_level/config
  ./test_dir/second_level/sTest2.py
  ./test_dir/second_level/stest1.py
  ./test_dir/second_level/stest3.sh
  ./test_dir/second_level/third_level
