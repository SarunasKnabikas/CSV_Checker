# CSV_Checker
Simple script to check CSV files before loading to DB.

This project is not using any external libraries. This makes it easy to deploy.

Main purpose to check CSV files in the most afficient way possible.

Script is tested for individual files sizes of 30MB+. 300MB is processed in about 90 seconds in the worst case scenarion.
It's use case is intended for smaller than 6MB CSV files. 30 files are processed in about 10 seconds.

## Checks done by script

1. Date format check
2. Begin (Sunday) and End (Saturday) date checks
3. Figures format check (whole and decimal)
4. Retailer name check against provided list (Parameters/Accounts.csv)
5. Column header check against provided list (Parameters/Headers.csv)
6. EAN duplicate check
7. EAN check agianst provided DB EAN list (Parameters/Ean_list.csv)
8. Product description check (Always must be "ABC")
9. Column number in row check. To ensure that comma or other symbols can't mess up the load.

## Results of running the script

1. CSV files in "Check" folder are run throught all the checks.
2. Files that pass all the checks are moved to folder "Correct".
3. Files that don't pass checks stay in the "Check" folder.
4. All rows are captured and added to new csv files into "Error" folder. Every row has a comment at the end what failed it.
5. Terminal show which files failed and which passed. Giving totals for all figure columns for files that passes the checks.

## Step-by-step: How to run the script
1. Windows: Add path to python.exe and path to script into batch file. This will allow to run script simply running batch file.
2. Script can be ran directly from CMD and PowerShell in windows and using terminal in other systems. Please google for specifics.
