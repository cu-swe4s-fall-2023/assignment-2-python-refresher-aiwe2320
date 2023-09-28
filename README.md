[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

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