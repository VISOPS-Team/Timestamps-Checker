# Timestamps-Checker
Timestamp Checker is a script that extracts the time of the first observation and time of the last observation from .obs files (typically used for GNSS data processing). The script can process .obs files from directories, sort them chronologically, and output the results into a CSV file for easy reference.
## Features
1. Extracts TIME OF FIRST OBS and TIME OF LAST OBS from .obs files.
2. Sorts .obs files chronologically by the time of first observation.
3. Outputs the results in a CSV file (time_observations_all.csv).
## Requirements
1. Python 3.x: Ensure Python is installed and available in your system's PATH.
2. Dependencies: 
    * os
    * csv
3. Folder Structure:
    * Ensure you have the rinex and rtk folders in your working directory.
    * The converted folders should be inside the rinex and rtk folders.
## Installation
1. Clone or Download the Repository
2. Ensure Python is installed 
      python --version
3. Copy the py file to your working directory and run

### 
1. Place both timestamp_checker.py and timestamp_checker.bat into a directory you want to run the script from.
   Example: C:\Users\skycatch\timestamp_checker
2. Edit the .bat file. Update the .bat file to use a relative path so it works from any location:
<pre> ```bat @echo off python C:\Users\skycatch\timestamp_checker\timestamps_checker.py %* ``` </pre>
3. Add the script directory to your System PATH
   a. Open the Start Menu and search for Environment Variables
   b. Under System Properties, click Environment Variables
   c. In System Variables, find and select Path, then click Edit
   d. Click New and add:
   C:\Users\skycatch\timestamp_checker
   e. Click OK to save and close all windows
4. To Run the Script Anywhere
   a. Navigate to your working directory
   b. Open Command Prompt and cd to your working folder
   c. Run the script by typing: timestamps_checker

  
