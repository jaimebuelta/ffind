Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $TESTDIR/../ffind/ffind.py sTest2 
  ./test_dir/second_level/sTest2.py
  $ $PYTHON $TESTDIR/../ffind/ffind.py --module "py_compile {}" sTest2 

Search for compiled file. Needs wildcard as python3 compiled file if different
  $ $PYTHON $TESTDIR/../ffind/ffind.py sTest2 
  ./test_dir/second_level/sTest2.py
  *sTest2*pyc (glob)

Error in the module
  $ $PYTHON $TESTDIR/../ffind/ffind.py --module "badmodule" stest3
  No module named badmodule
  [1]
