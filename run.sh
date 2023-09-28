#!/bin/bash

set -e
set -u
set -o pipefail

# Examples of print_fires.py usage
# Good Example
echo "Examples: print_fires.py"
echo " "
echo "Working Example"
echo "python print_fires.py --queryval Congo --querycol Area --resultcol 'Forest fires' --filename Agrofood_co2_emission.csv"
python print_fires.py --queryval Congo --querycol Area --resultcol 'Forest fires' --filename Agrofood_co2_emission.csv

set +e
# Error: File not found
echo " "
echo "Erroneous Example: File not found"
echo "Command: python print_fires.py --queryval 'United States of America' --querycol Area --resultcol 'Forest fires' --filename Agrofood_co2_emssion.csv"
python print_fires.py --queryval 'United States of America' --querycol Area --resultcol 'Forest fires' --filename Agrofood_co2_emssion.csv

# Error: Incorrect input (fake country)
echo " "
echo "Erroneous Example: Incorrect input (fake country)"
echo "Command: python print_fires.py --queryval 'Datlof' --querycol Area --resultcol 'Forest fires' --filename Agrofood_co2_emission.csv"
python print_fires.py --queryval 'Datlof' --querycol Area --resultcol 'Forest fires' --filename Agrofood_co2_emission.csv