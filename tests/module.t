Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $FFIND_PY sTest2 
  ./test_dir/second_level/sTest2.py
  $ $PYTHON $FFIND_PY --module "py_compile {}" sTest2 

Search for compiled file. Needs wildcard as python3 compiled file if different
  $ $PYTHON $FFIND_PY sTest2 
  ./test_dir/second_level/sTest2.py
  *sTest2*pyc (glob)

Error in the module
  $ $PYTHON $FFIND_PY --module "badmodule" stest3
  No module named badmodule
  [1]
