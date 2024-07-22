#!/bin/bash

# activate the virtual environment
. ./venv/bin/activate

# run the test suite
python -m pytest test_pink_morsel_visualizer.py

# collect exit code from pytest
# exit code is 0 if all tests pass
PYTEST_EXIT_CODE=$?

# return exit code 0 if all tests pass or 1 otherwise
if [ $PYTEST_EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi

#To run above code:
#1. Open Git Bash as administrator
#2. Navigate to the directory where test_pink_morsel_visualizer.py and run_tests.sh is saved using the cd command.
#3. Enter below commands:
#chmod +x run_tests.sh # Make Sure the Script is Executable
#./run_tests.sh # Run the Script


