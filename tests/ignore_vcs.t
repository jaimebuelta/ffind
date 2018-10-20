Setup

  $ . $TESTDIR/setup.sh

Run test

  $ $FFIND_CMD --hidden lib
  ./test_dir/.git/library
  ./test_dir/.venv/library
  $ $FFIND_CMD --hidden --ignore-vcs lib
  ./test_dir/.venv/library
  $ $FFIND_CMD lib

  $ $FFIND_CMD --hidden gitignore
  ./test_dir/.gitignore
  $ $FFIND_CMD --ignore-vcs gitignore

  $ $FFIND_CMD --hidden --ignore-vcs gitignore

Env variable

  $ FFIND_SEARCH_HIDDEN=1 $FFIND_CMD lib
  ./test_dir/.git/library
  ./test_dir/.venv/library
  $ FFIND_SEARCH_HIDDEN=1 FFIND_IGNORE_VCS=1 $FFIND_CMD lib
  ./test_dir/.venv/library
  $ FFIND_SEARCH_HIDDEN=1 $FFIND_CMD gitignore
  ./test_dir/.gitignore
  $ FFIND_IGNORE_VCS=1 $FFIND_CMD gitignore
