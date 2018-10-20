Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $PYTHON $FFIND_PY --hidden lib
  ./test_dir/.git/library
  ./test_dir/.venv/library
  $ $PYTHON $FFIND_PY --hidden --ignore-vcs lib
  ./test_dir/.venv/library
  $ $PYTHON $FFIND_PY lib

  $ $PYTHON $FFIND_PY --hidden gitignore
  ./test_dir/.gitignore
  $ $PYTHON $FFIND_PY --ignore-vcs gitignore

  $ $PYTHON $FFIND_PY --hidden --ignore-vcs gitignore

Env variable

  $ FFIND_SEARCH_HIDDEN=1 $PYTHON $FFIND_PY lib
  ./test_dir/.git/library
  ./test_dir/.venv/library
  $ FFIND_SEARCH_HIDDEN=1 FFIND_IGNORE_VCS=1 $PYTHON $FFIND_PY lib
  ./test_dir/.venv/library
  $ FFIND_SEARCH_HIDDEN=1 $PYTHON $FFIND_PY gitignore
  ./test_dir/.gitignore
  $ FFIND_IGNORE_VCS=1 $PYTHON $FFIND_PY gitignore
