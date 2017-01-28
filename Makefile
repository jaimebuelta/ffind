# The PYTHON env variable is passed to the tests
# Run the tests in python 3 only
test_python3:
	PYTHON=python3 cram -v tests/*.t

# Run the tests in python 3 only
test_python2:
	PYTHON=python cram -v tests/*.t

# For travis CI
travis:
	rm -f $(shell pwd)/.coverage
	COVERAGE_FILE='$(shell pwd)/.coverage' PYTHON='coverage run -a --source=ffind' cram -v tests/*.t

# Run the tests twice in Python 2 and 3
test: test_python3 test_python2
