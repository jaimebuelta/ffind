Setup

  $ . $TESTDIR/setup.sh

Run test, grep to reduce the output and standarize over different executions

  $ $PYTHON $TESTDIR/../ffind/ffind.py --module "trace --trace {}" sTest2 | grep sTest2
   --- modulename: sTest2, funcname: <module>
  sTest2.py(1): print("sTest2")
  sTest2
