Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $FFIND_CMD second
  ./test_dir/second_level

  $ $FFIND_CMD -p second
  ./test_dir/second_level
  ./test_dir/second_level/CVS
  ./test_dir/second_level/config
  ./test_dir/second_level/sTest2.py
  ./test_dir/second_level/stest1.py
  ./test_dir/second_level/stest3.sh
  ./test_dir/second_level/third_level

Using env variable

  $ FFIND_SEARCH_PATH=1 $FFIND_CMD second
  ./test_dir/second_level
  ./test_dir/second_level/CVS
  ./test_dir/second_level/config
  ./test_dir/second_level/sTest2.py
  ./test_dir/second_level/stest1.py
  ./test_dir/second_level/stest3.sh
  ./test_dir/second_level/third_level
