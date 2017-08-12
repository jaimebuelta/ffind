# Set a directory with different files to test search capabilities
TEST_DIR=./test_dir
mkdir $TEST_DIR
touch $TEST_DIR/test1.py
touch $TEST_DIR/Test2.py
touch $TEST_DIR/test3.sh
mkdir $TEST_DIR/second_level
echo 'inside of stest1' > $TEST_DIR/second_level/stest1.py
echo 'print("sTest2")' > $TEST_DIR/second_level/sTest2.py
touch $TEST_DIR/second_level/stest3.sh
touch $TEST_DIR/second_level/config
touch $TEST_DIR/second_level/.hidden
touch $TEST_DIR/second_level/CVS
mkdir $TEST_DIR/second_level/third_level
mkdir $TEST_DIR/.git
touch $TEST_DIR/.gitignore
touch $TEST_DIR/.git/config
touch $TEST_DIR/.git/library
mkdir $TEST_DIR/.venv
mkdir $TEST_DIR/.venv/library

FFIND_SORT=1
