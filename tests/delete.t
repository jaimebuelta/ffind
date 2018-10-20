Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $FFIND_CMD test1
  ./test_dir/test1.py
  ./test_dir/second_level/stest1.py
  $ $FFIND_CMD --delete stest1
  $ $FFIND_CMD test1
  ./test_dir/test1.py
  $ $FFIND_CMD third_level
  ./test_dir/second_level/third_level
  $ $FFIND_CMD --delete third_level
  $ $FFIND_CMD third_level
  $ $FFIND_CMD --delete second_level
  cannot delete: [Errno *] Directory not empty: './test_dir/second_level' (glob)
  [1]
