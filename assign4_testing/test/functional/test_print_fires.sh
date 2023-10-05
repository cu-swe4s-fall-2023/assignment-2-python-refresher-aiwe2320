test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run no_stat python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Forest fires' --filename ../data/Agrofood_test_data.csv
assert_stdout
assert_no_stderr
assert_exit_code 0

run test_mean python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Forest fires' --filename ../data/Agrofood_test_data.csv --stat mean
assert_in_stdout 4364.741
assert_exit_code 0

run test_median python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Forest fires' --filename ../data/Agrofood_test_data.csv --stat median
assert_in_stdout 3480
assert_exit_code 0

run test_stdev python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Forest fires' --filename ../data/Agrofood_test_data.csv --stat stdev
assert_in_stdout 4033.238
assert_exit_code 0

run test_mean_missing_entries python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Incomplete data' --filename ../data/Agrofood_test_data.csv --stat mean
assert_in_stdout 16.035
assert_exit_code 0

run test_median_missing_entries python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Incomplete data' --filename ../data/Agrofood_test_data.csv --stat median
assert_in_stdout 16.5
assert_exit_code 0

run test_stdev_missing_entries python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Incomplete data' --filename ../data/Agrofood_test_data.csv --stat stdev
assert_in_stdout 9.1
assert_exit_code 0

run test_mean_onlystrings python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Strings' --filename ../data/Agrofood_test_data.csv --stat mean
assert_in_stdout 'ERROR: Could not calculate mean'
assert_exit_code 1

run test_median_onlystrings python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Strings' --filename ../data/Agrofood_test_data.csv --stat median
assert_in_stdout 'ERROR: Could not calculate median'
assert_exit_code 1

run test_stdev_onlystrings python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Strings' --filename ../data/Agrofood_test_data.csv --stat stdev
assert_in_stdout 'ERROR: Could not calculate standard deviation'
assert_exit_code 1

run test_mean_mixeddata python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Mixed' --filename ../data/Agrofood_test_data.csv --stat mean
assert_in_stdout 15.5
assert_exit_code 0

run test_median_mixeddata python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Mixed' --filename ../data/Agrofood_test_data.csv --stat median
assert_in_stdout 16.5
assert_exit_code 0

run test_stdev_mixeddata python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Mixed' --filename ../data/Agrofood_test_data.csv --stat stdev
assert_in_stdout 9.33
assert_exit_code 0

run test_incorrect_filename python ../../src/print_fires.py --queryval Australia --querycol Area --resultcol 'Mixed' --filename ../data/Agrofood_test_data.cv --stat mean
assert_in_stderr 'No such file or directory'
assert_exit_code 1

run test_column_not_found python ../../src/print_fires.py --queryval Austria --querycol Area --resultcol 'Mixed' --filename ../data/Agrofood_test_data.csv
assert_in_stdout 'ERROR: Unable to process command inputs'
assert_exit_code 1

run test_column_not_found python ../../src/print_fires.py --queryval Austria --querycol Area --resultcol 'Area' --filename ../data/Agrofood_test_data.csv
assert_in_stdout 'Query column and result column are identical!'
assert_exit_code 1
