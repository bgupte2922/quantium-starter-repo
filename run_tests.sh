#!/bin/bash

# Activate the virtual environment (adjust the path if necessary)
source /path/to/your/virtualenv/bin/activate

# Navigate to your project directory (if not already there)
cd C:/Users/Bhagyashree/workspace_python/QuantiumSoftwareEngineeringVirtualInternship/quantium-starter-repo

# Run the test suite
python -m unittest discover -s tests/  # Replace with your actual test command

# Capture the exit code of the previous command
exit_code=$?

# Deactivate the virtual environment
deactivate

# Exit with the captured exit code
exit $exit_code