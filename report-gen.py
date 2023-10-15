import os
import csv
import time

# Define the directory where the log files are located
log_directory = "raw_outputs"

# Define the patterns to search for in the log files
patterns = ["EvtsPerSec[MECalcOnly]", "MAX_REG_COUNT"]

extracted_data = []

# Iterate over all files in the log directory
for filename in os.listdir(log_directory):
    log_file_name = os.path.join(log_directory, filename)

    # Initialize variables to store the matching lines
    data = {
            "Max Registers": None,
            "Block Number": None,
            "Epochs": None,
            "EvtsPerSec[MECalcOnly]": None,
    }

    # Open and read the log file
    with open(log_file_name, "r") as log_file:
        for line in log_file:
            for pattern in patterns:
                if "MAX_REG_COUNT" in line:
                    blocks = line.split(",")
                    data["Max Registers"] = blocks[0].split('=')[1].strip()
                    data["Block Number"] = blocks[1].split('=')[1].strip()
                    data["Epochs"] = blocks[2].split('=')[1].strip()

                elif "EvtsPerSec[MECalcOnly]" in line:
                    data["EvtsPerSec[MECalcOnly]"] = line.split('=')[1].strip().split(")")[0].split("(")[1].strip()

    extracted_data.append(data)

timestamp = int(time.time())
csv_file = f"experiment-{timestamp}.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Max Registers", "Block Number", "Epochs", "EvtsPerSec[MECalcOnly]"])
    writer.writeheader()
    for data in extracted_data:
        writer.writerow(data)
