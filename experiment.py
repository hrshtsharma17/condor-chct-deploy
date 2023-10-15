import subprocess

# Define lists of values for BLOCK_NUMBER, EPOCHS, and MAX_REG_COUNT
block_numbers = [108, 216]
epochs_values = [1]
max_reg_count_values = [120]

# Iterate over all combinations of values
for block_number in block_numbers:
    for epochs in epochs_values:
        for max_reg_count in max_reg_count_values:
            # Define the condor_submit command with variable assignments
            cmd = f"condor_submit job.submit BLOCK_NUMBER={block_number} EPOCHS={epochs} MAX_REG_COUNT={max_reg_count}"

            # Use subprocess to run the command
            try:
                subprocess.run(cmd, shell=True, check=True)
                print(f"Job submitted with BLOCK_NUMBER={block_number}, EPOCHS={epochs}, MAX_REG_COUNT={max_reg_count}")
            except subprocess.CalledProcessError as e:
                print(f"Error running the condor_submit command: {e}")
