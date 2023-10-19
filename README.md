[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

## get_column

The code herein is centered around the function get_column in my_utils.py.  get_column is a function designed to take a csv file, a query column, a query value, and a results column. The program will read the csv file and search the query column for the given query value. The function will return a list of integers (if possible) of all the corresponding results column values for all the query matches. The script print_fires.py implements this function with command line arguments. Run run.sh to see example usage of the print_fires.py script.  

print_fires.py Command Line Arguments:

--querycol : The queried column

--queryval : The value queried for in the query column

--resultcolumn : Column to pull results from for matching queries

--filename : Name of the csv file

Example use:
```
python print_fires.py --queryval Croatia --querycol Area --resultcol 'Forest fires' --filename Agrofood_co2_emission.csv
```

This will output a integer list of the number of forest fires in Croatia recorded by year.

Best Practices Changes:
- Implemented argparse to better handle command line arguments
- Removed print statements from get_column function
- Updated docustring to proper formatting
- Added main functions for both my_utils and print_fires
- Cut down and split up long lines for readability

Assignment 4 Changes:

Implemented statistical functions in my_utils and added an optional statistics flag (--stat) to print_fires to calculate the mean, median, or standard deviation of the data returned by the get_column function.  This methodology works broadly for any list and will return a value as long as there is at least one numerical entry in the list.  To test these changes to the my_utils and print_fires infrastructure, utilized unit and functional tests to evaluate function/program operations on different scenarios.  Used unit testing to test the statistical functions using uniform random distributions of integers and comparing calculated results to known statistical characteristics of a uniform distribution.  Additionally used functional testing and the Stupid Simple Bash Testing infrastructure to test varying edge cases of print_fires using a test csv file.


To run the new unit and functional tests from the main directory, run the following commands:

```
cd assign4_testing/test/unit
python -m unittest test_my_utils.py

cd assign4_testing/test/functional
source test_print_fires.sh
```


Assignment 5 Changes:

Implemented continuous integration through the inclusion of a .github/workflows directory.  The file tests.yml specifies that whenever a pull request or push to the master branch is done, unit tests, functional tests, and pycodestyle tests of my_utils.py and print_fires.py will be done.  This is to ensure functionality and best practices are maintained whenever changes are made.  The current CI setup utilizes conda to initialize an environment with pycodestyle, but this is slow and should be replaced with mamba to improve speeds.  Otherwise, all of the testing is conducted using ubuntu-latest as the shell.



Assignment 6 Changes:

I conducted an analysis of Australian forest fires versus total emissions.  To see the raw data and plots referenced here, see the directory /assign6_plotting/manual_analysis.

A histogram (AUS_fires.png) describing the frequency of forest fires showed that the distribution of fire frequency from 1990 to 2020 had a heavy tail.  The majority of years had a number of fires between 0 and about 4000 fires, with only about 25% of years having more than 4000 fires.

A scatter plot (AUS_emissions-year.png) of emissions versus year showed that Australia's total emissions had an overall downward trend over time.  However, there was significant variability in emissions, increasing or decreasing from year to year with no discernable pattern.  

A scatter plot (AUS_fires-year.png) of fores fire count versus year showed that Australia's number of fores fires was relatively consistent from 1990 to 2018, but spiked in 2019 and 2020.  The data analysis described herein cannot explain this spike and these years are likely outliers by chance or due to some cause not captured in this analysis.

A scatter plot (AUS_fires-emissions_scatter.png) of forest fire count versus total emissions suggests that the number of fires in Australia is independent of that year's total emissions.  Besides a few outliers, most of the data clumped in the same range of forest fire count irrespective of the total emissions value. 

Overall, this analysis of forest fires and total emissions by year in Australia is inconclusive.  There is no significant evidence to suggest that these variables are related year to year.  Expanding this analysis to other fire types (e.x. savanna fires) and specific energy and emissions data (e.x. agricultural electricity use) is needed to determine if there is any link between annual emissions and fires in Australia.


Update Log:

09/13/23 11:25AM:

Created the get_columns function with some minor input validation. The function requires input of a csv file delimited by commas and with column titles in the first line of the file.

Function definition:

my_utils.get_columns(file_name, query_column, query_value, result_column)

All arguments must be passed in as a string. The function will express if the file is empty, if either the query or result column is not present, or if no results matching the query value are found. Will throw an error if the file name is not found.


09/14/23 1:59PM:

Fixed print_fires.py such that it uses get_column to display the number of fires in the United States by year 


09/14/23 2:16PM:

Implemented named arguments for the usage of get_column in print_fires.py. Added default result column to get_column function definition. 
Additonally added a docustring to get_column to clarify its usage since I believe I implemented the function in a different way than the homework intended. 
get_column only takes strings as parameters.  The desired query and result column names must be entered, not an integer position in the csv file, which is what the original print_fires.py appeared to use.


09/14/23 2:25PM:

Minor print statement edit to print_fires.py and added run.sh that runs print_fires.py.


09/28/23 11:07AM:

Updated print_fires.py to use command line arguments and changed get_column function in my_utils.py to return a list of integers. This was accomplished using try:except logic, converting every string entry to the list to a float and then an integer via python list comprehension. 
Also removed print statements within the my_utils.py and tweaked print_fires.py to handle errors caught by get_column. If an input error is caught, get_column will return None. This removes specificity in pointing out the input errors, but removes side effects (print statements) from the get_column function.
Additionally updated run.sh to use command line arguments and gave 3 examples of proper/improper use of the print_fires.py script.


09/28/23 2:28PM:

Implemented best practices using pycodestyle as a guide, as well as lecture notes. Notably reformatted long lines and docustring, added main functions, and using argparse for cleaner command line arguments.


10/4/23  4:05PM:

Implemented statistical functions to calculate mean, median, and standard deviation from a list.  Statistical functions return None if unusable input.


10/4/23 6:45PM:

Implemented 12 unit tests to test the functionality of the statistical functions implemented in my_utils. 