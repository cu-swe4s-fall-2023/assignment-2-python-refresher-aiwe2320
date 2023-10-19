test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_get_data python ../../src/get_data.py --datafile ../../../Agrofood_co2_emission.csv --outfile Australia_fires.txt --country Australia --x_datacol 'Forest fires' --y_datacol 'total_emission'
assert_equal $"Australia_fires.txt" $( ls $"Australia_fires.txt" )
assert_exit_code 0

run test_hist python ../../src/hist.py --datafile ../../manual_analysis/Australia_fires.txt --data_label 'Number of Forest Fires' --col_ndx 1 --title 'Australian Forest Fires' --outfile 'AUS_fires.png'
assert_equal $"AUS_fires.png" $( ls $"AUS_fires.png" )
assert_exit_code 0

run test_scatter_emissison_year python ../../src/scatter.py --datafile ../../manual_analysis/Australia_fires.txt --x_col 0 --y_col 2 --x_label 'Year' --y_label 'Total Emissions' --title 'Australian Total Emissions by Year' --outfile 'AUS_emissions-year.png'
assert_equal $"AUS_emissions-year.png" $( ls $"AUS_emissions-year.png" )
assert_exit_code 0

run test_scatter_fires_year python ../../src/scatter.py --datafile ../../manual_analysis/Australia_fires.txt --x_col 0 --y_col 1 --x_label 'Year' --y_label 'Number of Forest Fires' --title 'Australian Forest Fires by Year' --outfile 'AUS_fires-year.png'
assert_equal $"AUS_fires-year.png" $( ls $"AUS_fires-year.png" )
assert_exit_code 0

run test_scatter_fires_emissions python ../../src/scatter.py --datafile ../../manual_analysis/Australia_fires.txt --x_col 2 --y_col 1 --x_label 'Total Emissions' --y_label 'Number Forest Fires' --title 'Australian Forest Fire Count vs Total Emissions' --outfile 'AUS_fires-emissions_scatter.png'
assert_equal $"AUS_fires-emissions_scatter.png" $( ls $"AUS_fires-emissions_scatter.png" )
assert_exit_code 0