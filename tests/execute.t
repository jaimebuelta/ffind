Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $FFIND_CMD --exec "cat" stest1
  inside of stest1
  $ $FFIND_CMD --exec "cat {}{}" stest1
  cat: ./test_dir/second_level/stest1.py./test_dir/second_level/stest1.py: No such file or directory
  [1]
