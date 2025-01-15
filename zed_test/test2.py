import os
import shutil
from datetime import datetime, timedelta

# Set your source and destination folders
source_folder = './history'
destination_folder = './history_sorted'
target_hour = 12  # Target hour (e.g., 18:00)
time_range = 20  # Time range in minutes (e.g., 18:00 ± 30 minutes)

# Ensure destination folder exists
os.makedirs(destination_folder, exist_ok=True)

def is_in_time_range(filename, target_hour, time_range):
    try:
        # Extract datetime from filename
        file_time = datetime.strptime(filename, "%Y-%m-%d-%H-%M.png")

        # Define the target range
        target_time = file_time.replace(hour=target_hour, minute=0)
        lower_bound = target_time - timedelta(minutes=time_range)
        upper_bound = target_time + timedelta(minutes=time_range)

        # Check if the file timestamp is within the specified time range
        return lower_bound <= file_time <= upper_bound
    except ValueError:
        # Ignore files that don't match the expected filename pattern
        return False

# Iterate through files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".png") and is_in_time_range(filename, target_hour, time_range):
        # Copy files that match the criteria
        src_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(destination_folder, filename)
        shutil.copy2(src_path, dest_path)
        print(f"Copied: {filename}")
