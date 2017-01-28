Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $TESTDIR/../ffind/ffind.py --module "trace --trace {}" sTest2
   --- modulename: sTest2, funcname: <module>
  sTest2.py(1): print("sTest2")
  sTest2
   --- modulename: trace, funcname: _unsettrace
  trace.py(*):         sys.settrace(None) (glob)
