def main():
    import my_utils
    import sys
    import argparse

    parser = argparse.ArgumentParser(
                description='Usage: print_fires.py --queryval QUERY_VALUE'
                            '--querycol QUERY_COLUMN --resultcol RESULT_COLUMN'
                            '--filename FILE_NAME',
                prog='print_fires')

    parser.add_argument('--filename',
                        type=str,
                        help='File name',
                        required=True)

    parser.add_argument('--querycol',
                        type=str,
                        help='Queried column',
                        required=True)

    parser.add_argument('--queryval',
                        type=str,
                        help='Value queried for in query column',
                        required=True)

    parser.add_argument('--resultcol',
                        type=str,
                        help='Column containing desired results',
                        required=True)

    args = parser.parse_args()
    country = args.queryval
    country_column = args.querycol
    fires_column = args.resultcol
    file_name = args.filename

    # Input validation
    if(country_column == fires_column):
        print("Query column and result column are identical!")
        sys.exit(1)

    year_col_name = 'Year'
    # get_column(file_name, query_column, query_value, result_column)
    forest_fires = my_utils.get_column(file_name=file_name,
                                       query_column=country_column,
                                       query_value=country,
                                       result_column=fires_column)
    # Get corresponding years matching fire search
    year_list = my_utils.get_column(file_name=file_name,
                                    query_column=country_column,
                                    query_value=country,
                                    result_column=year_col_name)

    if(forest_fires is None):
        print("ERROR: Unable to process command inputs")
        sys.exit(1)
    else:
        print(f'Total Forest Fires in {country} by Year:')
        print("Year: Fires")
        for i, item in enumerate(forest_fires):
            print(f'{year_list[i]}: {item}')


if __name__ == '__main__':
    main()
