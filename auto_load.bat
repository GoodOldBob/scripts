@echo OFF
rem print usage message
echo Usage: This script allows the user to run the python script 
echo "gomez_load_data.py" for any number of consecutive days. 
echo Make sure to use single digits if the day or month you are inputting 
echo is a single digit (e.g. 1 instead of 01 for January).
pause

rem take user input for year, month, and the first and last day
set /P $year="Enter year [YYYY]: "
set /P $month1="Enter the month of the first day [M or MM]: "
set /P $day1="Enter the first day [D or DD]: "
echo The first day to load data from is %$year%-%$month1%-%$day1%
set /P $month2="Enter the month of the last day [M or MM]: "
set /P $day2="Enter the last day [D or DD]: "
echo The last date to load data from is %$year%-%$month2%-%$day2%

rem calculate number of days to load data from
set /A "$dayDiff=%$day2%-%$day1%"
set /A "$monthDiff=%$month2%-%$month1%"

echo Loading %$dayDiff% days of data in %$monthDiff% month(s).

rem check if not in the same month
if [%$month1%]==[%$month2%] (
    for /L %%G in (%$day1%, 1, %$day2%) do ( 
        python gomez_load_data.py %$year%-%$month1%-%%G
    ) 
) else (
	set /P $monthLast="Please enter the last day of this month [DD]: "
    rem run the load data script for each month
    for /L %%H in (%$month1%, 1, %$month2%) do (
	    if [%%H]==[%$month1%] (
		    rem run the load data script for each day in the month
            for /L %%I in (%$day1%, 1, %$monthLast%) do ( 
                python gomez_load_data.py %$year%-%$month1%-%%I
            )
		rem if on last month then run the load data script until the final day
        ) else (
            for /L %%J in (1, 1, %$day2%) do ( 
                python gomez_load_data.py %$year%-%$month1%-%%J
            )
        )			
    )
)
