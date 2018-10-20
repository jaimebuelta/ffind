Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $FFIND_CMD sTest2 
  ./test_dir/second_level/sTest2.py
  $ $FFIND_CMD --module "py_compile {}" sTest2 

Search for compiled file. Needs wildcard as python3 compiled file if different
  $ $FFIND_CMD sTest2 
  ./test_dir/second_level/sTest2.py
  *sTest2*pyc (glob)

Error in the module
  $ $FFIND_CMD --module "badmodule" stest3
  No module named badmodule
  [1]
