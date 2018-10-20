Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $FFIND_PY test1
  ./test_dir/test1.py
  ./test_dir/second_level/stest1.py
  $ $PYTHON $FFIND_PY --delete stest1
  $ $PYTHON $FFIND_PY test1
  ./test_dir/test1.py
  $ $PYTHON $FFIND_PY third_level
  ./test_dir/second_level/third_level
  $ $PYTHON $FFIND_PY --delete third_level
  $ $PYTHON $FFIND_PY third_level
  $ $PYTHON $FFIND_PY --delete second_level
  cannot delete: [Errno *] Directory not empty: './test_dir/second_level' (glob)
  [1]
