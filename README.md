# Timestamp-Checker
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
         '''python --version


