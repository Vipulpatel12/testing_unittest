#!/bin/bash
# test_generation.sh

# Create directories if they don't exist
mkdir -p unit_test
modules=("testing_v1" "testing_v4")  # Replace with your actual module names

# Generate tests with Pynguin
# # Replace 'your_module' with the actual path to your module
for module in "${modules[@]}"; do
    echo "Generating tests for $module..."
    pynguin --project-path ./ \
            --output-path ./unit_test \
            --module-name $module \
            --algorithm DYNAMOSA \
            --maximum-search-time 10
done

# Organize generated tests
