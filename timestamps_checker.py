import os
import csv

def extract_time_obs(filename):
    """Extracts TIME OF FIRST OBS and TIME OF LAST OBS from a given file."""
    first_obs = None
    last_obs = None

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Check if line contains the "TIME OF FIRST OBS"
            if "TIME OF FIRST OBS" in line:
                first_obs = " ".join(line.split()[:6])  # Extract year, month, day, hour, minute, second
            # Check if line contains the "TIME OF LAST OBS"
            elif "TIME OF LAST OBS" in line:
                last_obs = " ".join(line.split()[:6])  # Extract year, month, day, hour, minute, second
            
            # If both first and last observations are found, stop processing further
            if first_obs and last_obs:
                break

    # Print debug information to verify timestamps
    print(f"Extracted - First Observation: {first_obs}, Last Observation: {last_obs}")
    return first_obs, last_obs

def process_obs_files(directory, file_list):
    """Processes .obs files in the given directory and appends data to the provided list."""
    for file in os.listdir(directory):
        if file.endswith(".obs"):
            file_path = os.path.join(directory, file)
            print(f"Processing file: {file_path}")
            first_obs, last_obs = extract_time_obs(file_path)
            if first_obs and last_obs:
                file_list.append([file, first_obs, last_obs])  # Store the file data for later processing
                print(f"Processed: {file} - First Observation: {first_obs}, Last Observation: {last_obs}")
            else:
                print(f"Could not extract timestamps from: {file}")

def sort_by_time(file_list):
    """Sort the file list chronologically by the first observation time."""
    return sorted(file_list, key=lambda x: x[1])  # Sort based on the first observation time (index 1)

# --- MAIN EXECUTION LOOP ---
output_csv = "time_observations_all.csv"
file_list = []  # This will hold the extracted data from both directories

# Check if the CSV exists, to avoid writing headers again
file_exists = os.path.isfile(output_csv)

# Automatically look for 'rinex' and 'rtk/converted' folders
rinex_folder = os.path.join(os.getcwd(), "rinex", "converted")
rtk_converted_folder = os.path.join(os.getcwd(), "rtk", "converted")

with open(output_csv, 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    if not file_exists:
        writer.writerow(["Filename", "TIME OF FIRST OBS", "TIME OF LAST OBS"])

    # Process rinex folder first (timestamps always at the top)
    if os.path.isdir(rinex_folder):
        print(f"Processing Rinex files in {rinex_folder}...")
        process_obs_files(rinex_folder, file_list)
        print(f"Data from Rinex folder added to list.")

    # Process rtk/converted folder next (timestamps ordered chronologically)
    rtk_converted_file_list = []  # This will hold the RTK converted files separately for sorting
    if os.path.isdir(rtk_converted_folder):
        print(f"Processing RTK converted files in {rtk_converted_folder}...")
        process_obs_files(rtk_converted_folder, rtk_converted_file_list)
        print(f"Data from RTK converted folder added to list.")

    # Sort the file list from rtk/converted folder chronologically
    sorted_rtk_file_list = sort_by_time(rtk_converted_file_list)

    # Write the data to the CSV file
    for file_data in file_list:
        writer.writerow(file_data)  # Write Rinex data first (as it is, no sorting)

    # Then, write the sorted RTK converted files
    for file_data in sorted_rtk_file_list:
        writer.writerow(file_data)

    print(f"All timestamps saved in {output_csv}")

