#!/bin/bash
# test_generation.sh

# Create directories if they don't exist
mkdir -p unit_test
modules=("testing_v1" "testing_v4")  # Replace with your actual module names


# Define a function to remove @pytest.mark.xfail(strict=True) from generated tests
remove_xfail_markers() {
    local test_dir=$1
    echo "Cleaning up xfail markers in $test_dir..."
    find "$test_dir" -type f -name "*.py" #-exec sed -i '' '/@pytest\.mark\.xfail(strict=True)/d' {} +
}

# Generate tests with Pynguin
# # Replace 'your_module' with the actual path to your module
for module in "${modules[@]}"; do
    echo "Generating tests for $module..."
    pynguin --project-path ./ \
            --output-path ./unit_test \
            --module-name $module \
            --algorithm DYNAMOSA \
            --maximum-search-time 10
    remove_xfail_markers "./unit_test"
done

# Organize generated tests
