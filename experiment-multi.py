import subprocess

# Define lists of values for BLOCK_NUMBER, EPOCHS, and MAX_REG_COUNT
block_numbers = [108, 216]
epochs_values = [30]
max_reg_count_values = [225, 240, 260, 280, 300, 320, 360, 400]

number_trails = 5

# Iterate over all combinations of values
for i in range(number_trails):
    for block_number in block_numbers:
        for epochs in epochs_values:
            for max_reg_count in max_reg_count_values:
                # Define the condor_submit command with variable assignments
                cmd = [
                        "condor_submit",
                        "job-multirun.submit",
                        "-a", f"block_number={block_number}",
                        "-a", f"epochs={epochs}",
                        "-a", f"max_reg_count={max_reg_count}"
                    ]

                print(cmd)
                try:
                    subprocess.run(cmd, check=True)
                    print(f"Job submitted with BLOCK_NUMBER={block_number}, EPOCHS={epochs}, MAX_REG_COUNT={max_reg_count}")
                except subprocess.CalledProcessError as e:
                    print(f"Error running the condor_submit command: {e}")
